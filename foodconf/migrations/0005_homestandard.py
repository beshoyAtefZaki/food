# Generated by Django 2.2.14 on 2020-09-10 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodconf', '0004_auto_20200905_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(blank=True, max_length=200, null=True)),
                ('unit_arabic_name', models.CharField(blank=True, max_length=200, null=True)),
                ('unit_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
