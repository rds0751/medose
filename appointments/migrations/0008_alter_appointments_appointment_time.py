# Generated by Django 3.2.9 on 2022-11-07 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_alter_appointments_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.TimeField(default=datetime.time(15, 6, 40, 319552), verbose_name='appointment time'),
        ),
    ]
