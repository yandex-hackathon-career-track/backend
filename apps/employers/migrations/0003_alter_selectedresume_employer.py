# Generated by Django 4.2.6 on 2023-10-28 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "employers",
            "0002_remove_employer_company_remove_employer_contacts_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="selectedresume",
            name="employer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="selected_resumes",
                to="employers.employer",
                verbose_name="Работодатель",
            ),
        ),
    ]