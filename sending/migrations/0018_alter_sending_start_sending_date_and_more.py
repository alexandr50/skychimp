# Generated by Django 4.2.1 on 2023-07-08 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0017_alter_sending_start_sending_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 8, 14, 30, 39, 750571), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(14, 30, 39, 750587), null=True, verbose_name='время рассылки'),
        ),
    ]