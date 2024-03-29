# Generated by Django 4.2.1 on 2023-07-07 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0013_alter_sending_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 7, 20, 24, 2, 436677), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(20, 24, 2, 436693), null=True, verbose_name='время рассылки'),
        ),
    ]
