import tempfile
from datetime import date

from django.http import HttpResponse

from PIL import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def format_experience(total_experience):
    """Преобразование месяцев в читаемый формат."""
    years = total_experience // 12
    months = total_experience % 12

    def pluralize(number, singular, plural1, plural2):
        if number == 1:
            return f"{number} {singular}"
        elif 2 <= number % 10 <= 4 and (
            number % 100 < 10 or number % 100 >= 20
        ):
            return f"{number} {plural1}"
        else:
            return f"{number} {plural2}"

    if years > 0 and months > 0:
        return (
            f"{pluralize(years, 'год', 'года', 'лет')} и "
            f"{pluralize(months, 'месяц', 'месяца', 'месяцев')}"
        )
    elif years > 0:
        return pluralize(years, "год", "года", "лет")
    elif months > 0:
        return pluralize(months, "месяц", "месяца", "месяцев")
    else:
        return "0 месяцев"


def calculate_total_experience(self):
    """Расчет общего опыта."""
    total_experience = 0
    job_dates = []

    for job in self.jobs.all():
        experience_months = job.experience

        if job.end_date is not None:
            for existing_job_dates in job_dates:
                if (
                    job.start_date <= existing_job_dates[1]
                    and job.end_date >= existing_job_dates[0]
                ):
                    overlapping_start = max(
                        job.start_date, existing_job_dates[0]
                    )
                    overlapping_end = min(job.end_date, existing_job_dates[1])
                    experience_months -= (
                        overlapping_end - overlapping_start
                    ).days // 30

        if experience_months > 0:
            total_experience += experience_months
            job_dates.append((job.start_date, job.end_date))

    return total_experience


def calculate_job_experience(start_date, end_date, is_current):
    """Расчет оыта от даты начала работы."""
    if is_current:
        today = date.today()
        delta = today - start_date
    elif end_date:
        delta = end_date - start_date
    else:
        return 0

    months = delta.days // 30
    return months


def generate_pdf(applicant, applicant_serializer):
    """Генерация PDF."""
    pdfmetrics.registerFont(TTFont("OpenSans", "static/fonts/open_sans.ttf"))
    response = HttpResponse(content_type="application/pdf")
    filename = f"applicant_{applicant.id}_resume.pdf"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    c = canvas.Canvas(response)
    x, y = 120, 800
    data = applicant_serializer.data

    def draw_text(text, size=12):
        nonlocal y
        c.setFont("OpenSans", size)
        c.drawString(30, y, text)
        y -= 20

    draw_text(f"{data['first_name']} {data['last_name']}", size=23)
    y -= 5

    draw_text(data["direction"]["name"], size=14)

    draw_text(
        f"Опыт работы - {format_experience(data['total_experience'])}", size=14
    )

    y -= 10
    draw_text("Должность:", size=17)
    for job_item in data["jobs"]:
        draw_text(
            f"{job_item['name']} - {format_experience(job_item['experience'])}",
            size=12,
        )
    y -= 10

    draw_text("Курсы:", size=17)
    for course in data["applicant_courses"]:
        draw_text(
            f"{course['course']},  дата окончания: {course['graduation_date']}",
            size=12,
        )
    y -= 10

    draw_text("Образование:", size=17)
    for education in data["educations"]:
        draw_text(f"{education['name']}", size=12)
    y -= 10

    draw_text("Навыки:", size=17)
    stack_items = [stack_item["name"] for stack_item in data.get("stack", [])]
    stack_string = ", ".join(stack_items)
    draw_text(f"Стек: {stack_string}", size=12)
    y -= 10

    draw_text("Формат работы и город", size=17)
    for work_format in data["work_format"]:
        draw_text(f"Формат работы: {work_format['name']}", size=12)
    for occupation in data["occupation"]:
        draw_text(f"Занятость: {occupation['name']}", size=12)
    draw_text(f"Город: {data['city']}", size=12)
    y -= 10

    draw_text("Портфолио и сертификаты", size=17)
    for portfolio_link in data["portfolio_links"]:
        draw_text(
            f"{portfolio_link['name']}, {portfolio_link['link']}", size=12
        )
    y -= 10

    draw_text("Контакты", size=17)
    contacts = data.get("contact", {})
    if "telegram" in contacts:
        draw_text(f"Telegram: {contacts['telegram']}", size=12)
    if "email" in contacts:
        draw_text(f"Email: {contacts['email']}", size=12)
    if applicant.photo:
        photo = Image.open(applicant.photo.path)
        desired_width, desired_height = 150, 200
        x, y = 420, 820
        width, height = photo.size
        scale = min(desired_width / width, desired_height / height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        photo = photo.resize((new_width, new_height), Image.LANCZOS)

        x += (desired_width - new_width) / 2
        y -= desired_height

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".png"
        ) as temp_file:
            photo.save(temp_file, "PNG")
            temp_file.seek(0)
            photo_path = temp_file.name

        c.drawImage(
            photo_path,
            x,
            y,
            width=new_width,
            height=new_height,
        )
    c.showPage()
    c.save()

    return response
