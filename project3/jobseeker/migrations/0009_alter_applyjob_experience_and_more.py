# Generated by Django 5.0.1 on 2024-02-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0008_alter_applyjob_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='experience',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='regmodel',
            name='uname',
            field=models.CharField(max_length=200),
        ),
    ]