# Generated by Django 2.2.13 on 2022-11-16 00:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fdadb', '0004_auto_20221116_0256'),
        ('appointments', '0019_auto_20221116_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='medicineb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='fdadb.MedicationName'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.TimeField(default=datetime.time(5, 47, 32, 298046), verbose_name='appointment time'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='medicine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointments.Medicine'),
        ),
    ]