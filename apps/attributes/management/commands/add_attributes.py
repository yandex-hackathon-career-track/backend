import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from apps.attributes.models import (
    ActivityStatus,
    Direction,
    City,
    Course,
    Stack,
    ReviewStatus,
    WorkFormat,
    Occupation,
)


class Command(BaseCommand):
    help = "Fills database with the fixtures of attributes"

    def handle(self, *args, **kwargs):
        FILE_HANDLE = (
            ("directions.csv", Direction),
            ("cities.csv", City),
            ("stack.csv", Stack),
            ("work_formats.csv", WorkFormat),
            ("occupations.csv", Occupation),
            ("courses.csv", Course),
            ("activity_status.csv", ActivityStatus),
            ("review_status.csv", ReviewStatus),
        )
        for file, model in FILE_HANDLE:
            self.stdout.write(f'{"---"*40}\nОткрываем файл {file}')
            file_path = Path("static", "fixtures", file)
            if not file_path.exists():
                self.stderr.write(f"Файл {file} не найден")
                continue
            with open(file_path, mode="r", encoding="utf8") as f:
                self.stdout.write(f"Начинаем импорт из файла {file}")
                reader = csv.DictReader(f, delimiter=";")
                counter = 0
                objects_to_create = []
                for row in reader:
                    counter += 1
                    args = dict(**row)
                    try:
                        objects_to_create.append(model(**args))
                    except TypeError:
                        self.stderr.write("Неверный заголовок в csv-файле")
                        break
                try:
                    model.objects.bulk_create(
                        objects_to_create, ignore_conflicts=True
                    )
                    self.stdout.write(
                        f"Добавлено объектов: {len(objects_to_create)}; "
                        f"строк в документе: {counter}"
                    )
                except ValueError:
                    self.stderr.write("Ошибка заполнения csv. Импорт отменен")
