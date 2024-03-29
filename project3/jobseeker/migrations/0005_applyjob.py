# Generated by Django 5.0.1 on 2024-02-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0004_rename_fname_regmodel_date_rename_lname_regmodel_heq_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]
