# Generated by Django 5.1.3 on 2024-11-28 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regulatorydocuments',
            name='name_document',
            field=models.CharField(max_length=150, null=True, verbose_name='укажите имя документа'),
        ),
    ]
