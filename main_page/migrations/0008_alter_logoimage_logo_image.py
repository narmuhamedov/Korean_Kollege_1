# Generated by Django 5.1.1 on 2024-09-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0007_advanced"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logoimage",
            name="logo_image",
            field=models.ImageField(
                null=True, upload_to="logo_images", verbose_name="Загрузите фото лого"
            ),
        ),
    ]
