# Generated by Django 3.2.9 on 2022-11-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0010_auto_20210224_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='voucherapplication',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='voucherset',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
