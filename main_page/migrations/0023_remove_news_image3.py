# Generated by Django 5.1.2 on 2024-11-24 07:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0022_news_views"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="image3",
        ),
    ]