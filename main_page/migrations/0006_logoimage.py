# Generated by Django 5.1.1 on 2024-09-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0005_alter_itcourses_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogoImage",
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
                ("logo_image", models.ImageField(upload_to="logo_images")),
            ],
        ),
    ]
