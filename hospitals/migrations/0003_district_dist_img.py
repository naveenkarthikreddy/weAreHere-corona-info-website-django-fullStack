# Generated by Django 3.2 on 2021-05-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_alter_state_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='dist_img',
            field=models.ImageField(default='blank', upload_to='district/images'),
        ),
    ]
