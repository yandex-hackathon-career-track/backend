# Generated by Django 4.2.6 on 2023-10-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attributes", "0004_alter_direction_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeesNumber",
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
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Численность сотрудников",
                "verbose_name_plural": "Численность сотрудников",
            },
        ),
        migrations.AlterModelOptions(
            name="course",
            options={
                "verbose_name": "Курс Практикума",
                "verbose_name_plural": "Курсы Практикума",
            },
        ),
        migrations.RemoveField(
            model_name="activitystatus",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="activitystatus",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="city",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="city",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="course",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="course",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="direction",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="direction",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="occupation",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="occupation",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="reviewstatus",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="reviewstatus",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="stack",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="stack",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="workformat",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="workformat",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="activitystatus",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="direction",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="occupation",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="reviewstatus",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="stack",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="workformat",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название"
            ),
        ),
    ]
