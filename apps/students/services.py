import pandas as pd

from django.db.models import QuerySet
from django.http import HttpResponse


def get_dataframe(applicants: QuerySet) -> pd.DataFrame:
    """Подготовка данных для записи к Excel"""

    data = []
    for person in applicants:
        applicant_data = {
            "Имя Фамилия": f"{person.first_name} {person.last_name}",
            # "Должность": person.direction,
            "Статус": person.status,
            "Контакты": f"{person.contact.email}; {person.contact.telegram}",
            "Город": person.city,
            "Опыт": f"{person.total_experience} мес.",
            "Навыки/Инструменты": ", ".join(
                [tool.name for tool in person.stack.all()]
            ),
            "Формат работы": ", ".join(
                [item.name for item in person.work_format.all()]
            ),
            "Занятость": ", ".join(
                [item.name for item in person.occupation.all()]
            ),
            "Курсы": "\n".join(
                [
                    f"{item.course.name} ({item.graduation_date})"
                    for item in person.applicant_courses.all()
                ]
            ),
            "Работа": "\n".join(
                [
                    f"{job.name} ({job.experience} мес.)"
                    for job in person.jobs.all()
                ]
            ),
            "Образование": "\n".join(
                [edu.name for edu in person.educations.all()]
            ),
            "Портфолио": "\n".join(
                [item.link for item in person.portfolio_links.all()]
            ),
        }
        data.append(applicant_data)
    return pd.DataFrame(data)


def render_response_with_report(applicants: QuerySet) -> HttpResponse:
    dataframe = get_dataframe(applicants)

    filename = "applicants.xlsx"
    response = HttpResponse(content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = f"attachment; filename={filename}"

    with pd.ExcelWriter(response, engine="xlsxwriter") as writer:
        dataframe.to_excel(writer, sheet_name="applicants", index=False)
        workbook = writer.book
        worksheet = writer.sheets["applicants"]
        worksheet.set_zoom(90)
        workbook.add_format({"align": "right", "bold": True, "bottom": 6})
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 10)
        worksheet.set_column("C:C", 26)
        worksheet.set_column("D:D", 12)
        worksheet.set_column("E:E", 8)
        worksheet.set_column("F:F", 32)
        worksheet.set_column("G:H", 23)
        worksheet.set_column("I:K", 35)
        worksheet.set_column("L:L", 20)
    return response
