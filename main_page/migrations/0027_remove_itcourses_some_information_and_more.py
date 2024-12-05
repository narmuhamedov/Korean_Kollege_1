# Generated by Django 5.1.3 on 2024-11-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0026_remove_courses_some_information"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itcourses",
            name="some_information",
        ),
        migrations.AddField(
            model_name="courses",
            name="qualification",
            field=models.CharField(
                max_length=100, null=True, verbose_name="укажите квалификацию"
            ),
        ),
        migrations.AddField(
            model_name="courses",
            name="year_study",
            field=models.CharField(
                max_length=100, null=True, verbose_name="укажите срок обучения"
            ),
        ),
        migrations.AddField(
            model_name="itcourses",
            name="qualification",
            field=models.CharField(
                max_length=100, null=True, verbose_name="укажите квалификацию"
            ),
        ),
        migrations.AddField(
            model_name="itcourses",
            name="year_study",
            field=models.CharField(
                max_length=100, null=True, verbose_name="укажите срок обучения"
            ),
        ),
    ]