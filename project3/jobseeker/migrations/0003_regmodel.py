# Generated by Django 5.0.1 on 2024-02-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0002_jobapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]