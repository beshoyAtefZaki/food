# Generated by Django 2.2.14 on 2020-10-02 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_auto_20201002_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='strat_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 20, 0, 59, 698448)),
        ),
    ]