# Generated by Django 5.1.2 on 2024-11-08 18:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0015_opendoor"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="itcourses",
            options={
                "permissions": [("can_add_it_courses", "Может добавлять IT курсы")],
                "verbose_name": "IT направление",
                "verbose_name_plural": "IT направления",
            },
        ),
    ]