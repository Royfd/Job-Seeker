# Generated by Django 5.0.1 on 2024-02-27 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0010_rename_phone_number_applyjob_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='resume',
            field=models.FileField(upload_to='jobseeker/static'),
        ),
    ]