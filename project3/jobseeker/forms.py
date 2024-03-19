from django import forms
from .models import *


class JobApplicationForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    job_title = forms.CharField(max_length=100)
    work_type = forms.CharField(max_length=50)
    experience = forms.CharField(max_length=100)
    job_type = forms.CharField(max_length=50)


class reggform(forms.ModelForm):
    class Meta:
        model = regmodel
        fields = "__all__"


class applyform(forms.ModelForm):
    class Meta:
        model = applyyjob
        fields = "__all__"


class loginn(forms.Form):
    email = forms.EmailField()
    pas = forms.CharField(max_length=20)




class contactform(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    subject = forms.CharField(max_length=100)
