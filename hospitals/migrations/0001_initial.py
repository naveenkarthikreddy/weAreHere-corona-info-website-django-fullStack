# Generated by Django 3.2.2 on 2021-05-17 16:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no_of_the_ambulance', models.CharField(max_length=30)),
                ('name_of_the_ambulance_driver', models.CharField(max_length=30)),
                ('contact_no_of_ambulance_driver', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('pincode', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('gmap_link', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_hospital', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('gmap_link', models.CharField(max_length=2048)),
                ('pincode', models.IntegerField()),
                ('total_icu_beds', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_icu_ventilator_beds', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_o2_beds', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_normal_beds', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('contact_number_of_the_hospital', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dist', to='hospitals.district')),
            ],
        ),
        migrations.CreateModel(
            name='oxygen_cylinders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_oxygen_dealer', models.CharField(max_length=30)),
                ('contact_no_of_the_oxygen_dealer', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('pincode', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('gmap_link', models.CharField(max_length=2048)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.district')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StaffData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
                ('contact', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
                ('ambulance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.ambulances')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.hospital')),
                ('oxygen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.oxygen_cylinders')),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_medical_store', models.CharField(max_length=30)),
                ('name_of_the_shop_owner', models.CharField(max_length=30)),
                ('contact_no_of_the_medical_shop_owner', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('pincode', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('gmap_link', models.CharField(max_length=2048)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.district')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField()),
                ('icu_beds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('o2_beds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('normal_beds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.hospital')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.state'),
        ),
        migrations.AddField(
            model_name='ambulances',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.district'),
        ),
    ]
