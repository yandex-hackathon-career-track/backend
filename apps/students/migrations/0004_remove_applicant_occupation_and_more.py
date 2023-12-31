# Generated by Django 4.2.6 on 2023-10-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attributes", "0003_occupation"),
        (
            "students",
            "0003_remove_applicant_can_relocate_applicant_occupation",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applicant",
            name="occupation",
        ),
        migrations.RemoveField(
            model_name="applicant",
            name="work_format",
        ),
        migrations.AddField(
            model_name="applicant",
            name="occupation",
            field=models.ManyToManyField(
                to="attributes.occupation", verbose_name="Тип занятости"
            ),
        ),
        migrations.AddField(
            model_name="applicant",
            name="work_format",
            field=models.ManyToManyField(
                to="attributes.workformat", verbose_name="Формат работы"
            ),
        ),
    ]
