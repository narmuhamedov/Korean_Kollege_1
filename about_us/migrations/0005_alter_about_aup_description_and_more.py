# Generated by Django 5.1.2 on 2024-11-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("about_us", "0004_about_aup_achievements_about_aup_education_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about_aup",
            name="description",
            field=models.TextField(verbose_name="укажите научную степень"),
        ),
        migrations.AlterField(
            model_name="about_ppc",
            name="description",
            field=models.TextField(verbose_name="укажите научную степень"),
        ),
    ]