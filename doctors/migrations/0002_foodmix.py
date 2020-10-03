# Generated by Django 2.2.14 on 2020-09-29 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodconf', '0011_auto_20200929_1605'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('home_standrd', models.CharField(blank=True, max_length=200, null=True)),
                ('home_standrd_wieght', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('standard_unit_count', models.DecimalField(decimal_places=2, default=1, max_digits=10, null=True)),
                ('refuse', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('water', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('enerygy', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ASH', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fiber', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Carbohydrate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sodium', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('potasium', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Calcium', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('phorphorus', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('magnisum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('iron', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('zinc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('coper', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vitamen_a', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vitamen_c', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('thiamen', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('riboflabn', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ingredients', models.ManyToManyField(to='doctors.MsureUnit')),
                ('item_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodconf.ItemGroup')),
                ('standard_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodconf.Choises')),
            ],
        ),
    ]
