# Generated by Django 4.2.3 on 2024-11-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0014_mission_alter_news_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="OpenDoor",
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
                    "open_door",
                    models.TextField(verbose_name="укажите почему выбирают нас"),
                ),
            ],
            options={
                "verbose_name": "выбирают нас",
                "verbose_name_plural": "выбрали нас",
            },
        ),
    ]