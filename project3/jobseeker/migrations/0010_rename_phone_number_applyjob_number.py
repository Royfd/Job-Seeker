# Generated by Django 5.0.1 on 2024-02-26 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0009_alter_applyjob_experience_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applyjob',
            old_name='phone_number',
            new_name='number',
        ),
    ]