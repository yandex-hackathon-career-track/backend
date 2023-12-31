# Generated by Django 4.2.6 on 2023-10-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "attributes",
            "0002_activitystatus_reviewstatus_alter_course_options_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Occupation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата обновления"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название"),
                ),
            ],
            options={
                "verbose_name": "Тип занятости",
                "verbose_name_plural": "Типы занятости",
            },
        ),
    ]
