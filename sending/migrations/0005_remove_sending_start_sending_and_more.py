# Generated by Django 4.2.1 on 2023-07-05 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0004_alter_sending_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sending',
            name='start_sending',
        ),
        migrations.AddField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 5, 13, 7, 11, 364385), verbose_name='Время начала'),
        ),
        migrations.AddField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, null=True, verbose_name='время рассылки'),
        ),
    ]