# Generated by Django 5.1.3 on 2024-11-28 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0025_alter_news_image3"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="courses",
            name="some_information",
        ),
    ]
