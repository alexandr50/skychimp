# Generated by Django 4.2.1 on 2023-07-06 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0007_alter_sending_start_sending_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 6, 19, 44, 17, 72204), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(19, 44, 17, 72227), null=True, verbose_name='время рассылки'),
        ),
    ]
