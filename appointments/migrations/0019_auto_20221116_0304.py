# Generated by Django 2.2.13 on 2022-11-15 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0018_auto_20221116_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.TimeField(default=datetime.time(3, 4, 16, 825867), verbose_name='appointment time'),
        ),
    ]