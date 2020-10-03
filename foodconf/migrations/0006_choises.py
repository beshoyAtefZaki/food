# Generated by Django 2.2.14 on 2020-09-28 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodconf', '0005_homestandard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arabic_name', models.CharField(blank=True, max_length=200, null=True)),
                ('english_name', models.CharField(blank=True, max_length=200, null=True)),
                ('number_of_home_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
