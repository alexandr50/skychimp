# Generated by Django 4.2.1 on 2023-07-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0003_remove_sending_end_sending_sending_next_run'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время создания'),
        ),
    ]