from django.db import models
from django.contrib.auth.models import User


class profile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    job_title = models.CharField(max_length=100)
    work_type = models.CharField(max_length=50)
    experience = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)


class applyyjob(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    qualification = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    resume = models.FileField(upload_to="jobseeker/static")


class regmodel(models.Model):
    uname = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    heq = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
