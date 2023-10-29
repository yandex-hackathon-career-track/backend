import pandas as pd

from django.db.models import QuerySet


def get_dataframe(applicants: QuerySet) -> pd.DataFrame:
    """Подготовка данных для записи к Excel"""

    data = []
    for person in applicants:
        applicant_data = {
            "Имя Фамилия": f"{person.first_name} {person.last_name}",
            # "Должность": person.direction,
            "Статус": person.status,
            "Контакты": f"{person.contact.email} {person.contact.telegram}",
            "Город": person.city,
            "Опыт": person.total_experience,
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
                [f"{job.name} ({job.experience})" for job in person.jobs.all()]
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
