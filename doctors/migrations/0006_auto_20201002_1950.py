# Generated by Django 2.2.14 on 2020-10-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_doctorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='image',
            field=models.ImageField(upload_to='doctors/profil'),
        ),
    ]
