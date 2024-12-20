# Generated by Django 5.1.2 on 2024-11-12 03:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0003_remove_normative_legal_acts_file_doc_category_acts"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category_acts",
            options={
                "verbose_name": "Категорию актов",
                "verbose_name_plural": "Категории актов",
            },
        ),
        migrations.RemoveField(
            model_name="category_acts",
            name="file_doc",
        ),
        migrations.RemoveField(
            model_name="license",
            name="file_doc",
        ),
        migrations.RemoveField(
            model_name="organizational_structure",
            name="file_doc",
        ),
        migrations.AddField(
            model_name="category_acts",
            name="url_doc",
            field=models.URLField(
                null=True, verbose_name="Укажите путь из DRIVE из нужного акта"
            ),
        ),
        migrations.AddField(
            model_name="license",
            name="url_doc",
            field=models.URLField(
                null=True, verbose_name="Укажите путь из DRIVE для лицензии"
            ),
        ),
        migrations.AddField(
            model_name="organizational_structure",
            name="url_doc",
            field=models.URLField(
                null=True,
                verbose_name="Укажите путь из DRIVE для Организационной структуры",
            ),
        ),
    ]
