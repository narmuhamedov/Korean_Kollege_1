# Generated by Django 5.1.2 on 2024-11-08 19:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0019_alter_advanced_options_alter_contact_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="advanced",
            options={
                "verbose_name": "продвижение",
                "verbose_name_plural": "продвижения",
            },
        ),
        migrations.AlterModelOptions(
            name="contact",
            options={"verbose_name": "контакт", "verbose_name_plural": "контакты"},
        ),
        migrations.AlterModelOptions(
            name="courses",
            options={
                "verbose_name": "направление",
                "verbose_name_plural": "направления",
            },
        ),
        migrations.AlterModelOptions(
            name="itcourses",
            options={
                "verbose_name": "IT направление",
                "verbose_name_plural": "IT направления",
            },
        ),
        migrations.AlterModelOptions(
            name="logoimage",
            options={
                "verbose_name": "фото лого",
                "verbose_name_plural": "фото логотипа",
            },
        ),
        migrations.AlterModelOptions(
            name="mission",
            options={"verbose_name": "миссия", "verbose_name_plural": "миссии"},
        ),
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name": "новость", "verbose_name_plural": "новости"},
        ),
        migrations.AlterModelOptions(
            name="opendoor",
            options={
                "verbose_name": "выбирают нас",
                "verbose_name_plural": "выбрали нас",
            },
        ),
        migrations.AlterModelOptions(
            name="welcome",
            options={
                "verbose_name": "добро пожаловать",
                "verbose_name_plural": "добро пожаловать",
            },
        ),
    ]
