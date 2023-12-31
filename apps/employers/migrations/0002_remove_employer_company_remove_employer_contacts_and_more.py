# Generated by Django 4.2.6 on 2023-10-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employer",
            name="company",
        ),
        migrations.RemoveField(
            model_name="employer",
            name="contacts",
        ),
        migrations.AddField(
            model_name="employer",
            name="about",
            field=models.TextField(
                blank=True, max_length=1000, verbose_name="О компании"
            ),
        ),
        migrations.AddField(
            model_name="employer",
            name="activity",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Сфера деятельности"
            ),
        ),
        migrations.AddField(
            model_name="employer",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Контактный email"
            ),
        ),
        migrations.AddField(
            model_name="employer",
            name="name",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Название компании"
            ),
        ),
        migrations.AddField(
            model_name="employer",
            name="phone",
            field=models.CharField(
                blank=True, max_length=20, verbose_name="Номер телефона"
            ),
        ),
        migrations.AddField(
            model_name="employer",
            name="website",
            field=models.URLField(blank=True, verbose_name="Ссылка на сайт"),
        ),
        migrations.DeleteModel(
            name="Company",
        ),
    ]
