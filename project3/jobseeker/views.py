from django.shortcuts import render, redirect
from .models import *
from project3.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
import uuid
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import *


def homme(request):
    return render(request, 'homee.html')


def regis(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pas = request.POST.get('password')
        if User.objects.filter(username=uname).first():
            messages.success(request, "username already taken")
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request, "email already taken")
            return redirect(regis)
        user_obj = User(username=uname, email=email)
        user_obj.set_password(pas)
        user_obj.save()

        auth_token = str(uuid.uuid4())
        profile_obj = profile1.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email, auth_token)
        return redirect(success)
    return render(request, 'register.html')


def success(request):
    return render(request, "success.html")


def lo(request):
    global User;
    if request.method == 'POST':
        username = request.POST.get('uname')
        pas = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect(lo)
        profile_obj = profile1.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified check ur email')
            return redirect(lo)
        User = authenticate(username=username, password=pas)
        if User is None:
            messages.success(request, 'wrong password or username')
            return redirect(lo)
        obj = profile1.objects.filter(user=user_obj)
        return render(request, 'home2.html', {'obj': obj})
    return render(request, 'companylogin.html')


def verify(request, auth_token):
    profile_obj = profile1.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request, 'your account is already verified')
            redirect(lo)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'ur account is verified')
        return redirect(lo)
    else:
        return redirect(error)


def error(request):
    return render(request, 'error.html')


def send_mail_regis(email, token):
    subject = "your account has been verified"
    message = f'pass the link to verify your account  http://127.0.0.1:8000/verify/{token}'
    email_from = EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)


def jobapplication(request, id):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            cnm = form.cleaned_data['company_name']
            eml = form.cleaned_data['email']
            jt = form.cleaned_data['job_title']
            wt = form.cleaned_data['work_type']
            ex = form.cleaned_data['experience']
            jtp = form.cleaned_data['job_type']
            b = JobApplication(company_name=cnm, email=eml, job_title=jt, work_type=wt, experience=ex, job_type=jtp)
            b.save()
            return HttpResponse("added")
        else:
            return HttpResponse("ENTER VALID DATA")
    form = profile1.objects.get(id=id)
    return render(request, 'addjob.html', {'obj': form})


def reg(request):
    if request.method == 'POST':
        a = reggform(request.POST)
        if a.is_valid():
            unm = a.cleaned_data['uname']
            eml = a.cleaned_data['email']
            num = a.cleaned_data['number']
            d = a.cleaned_data['date']
            eq = a.cleaned_data['heq']
            pas = a.cleaned_data['password']
            cpass = a.cleaned_data['cpassword']
            if pas == cpass:
                b = regmodel(uname=unm, email=eml, number=num, date=d, heq=eq, password=pas)
                b.save()
                return HttpResponse("successfully registered")
            else:
                return HttpResponse("password and cpassword is not match")
        else:
            return HttpResponse("enter valid data")
    return render(request, 'register2.html')


def logins(request):
    if request.method == 'POST':
        form = loginn(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['pas']
            user = regmodel.objects.filter(email=email, password=password).first()
            if user:
                return render(request, 'login.html', {'user': user})
            else:
                return HttpResponse("email and password incorrect......")
        else:
            return HttpResponse("enter valid data")
    else:
        return render(request, 'jobseekerlogin.html')


def edit(request, id):
    user = regmodel.objects.get(id=id)
    if request.method == 'POST':
        user.uname = request.POST.get('uname')
        user.email = request.POST.get('email')
        user.number = request.POST.get('number')
        user.date = request.POST.get('date')
        user.heq = request.POST.get('heq')
        user.save()
        return redirect(logins)
    return render(request, 'editprofile.html', {'user': user})


def updates(request, id):
    if request.method == 'POST':
        reg = regmodel.objects.get(id=id)
        f = reggform(request.POST, instance=reg)
        if f.is_valid():
            f.save()
            return redirect(show)
        else:
            return HttpResponse("enter valid data")


def show(request):
    return render(request, 'jobseekerlogin.html')


def openings(request, id):
    a = JobApplication.objects.all()
    uid = id
    return render(request, "openings.html", {'a': a, 'uid': uid})


def jobdt(request, id1, id2):
    user = JobApplication.objects.get(id=id1)
    uid = id2
    return render(request, 'jobdt.html', {'user': user, 'uid': uid})


def applyy(request, id1, id2):
    user = JobApplication.objects.get(id=id1)
    u = applyyjob.objects.get(id=id2)

    if request.method == 'POST':
        cn = request.POST.get('company_name')
        un = request.POST.get('name')
        jt = request.POST.get('job_title')
        em = request.POST.get('email')
        q = request.POST.get('qualification')
        n = request.POST.get('number')
        e = request.POST.get('experience')
        r = request.FILES.get('resume')
        b = applyyjob(company_name=cn, name=un, job_title=jt, email=em, qualification=q, number=n, experience=e,
                     resume=r)
        b.save()
        return HttpResponse("Submitted")
    return render(request, 'applyform.html', {'user': user, 'u': u})


def view_applicant(request, id):
    userr = profile1.objects.get(id=id)
    cname = userr.user.username
    a = applyyjob.objects.all()
    job_title = []
    name = []
    email = []
    qualification = []
    number = []
    experience = []
    resume = []
    for i in a:
        if i.company_name == cname:
            jobtitle1 = i.job_title
            job_title.append(jobtitle1)
            name1 = i.name
            name.append(name1)
            email1 = i.email
            email.append(email1)
            qualification1 = i.qualification
            qualification.append(qualification1)
            number1 = i.number
            number.append(number1)
            experience1 = i.experience
            experience.append(experience1)
            resume1 = i.resume
            resume.append(str(resume1).split('/')[-1])
    applicants = zip(job_title, name, email, qualification, number, experience, resume)
    return render(request, 'applicants.html', {'applicants': applicants})


def applied(request, id):
    a = applyyjob.objects.all()
    b = regmodel.objects.get(id=id)
    name1 = b.uname
    job_title = []
    company_name = []
    for i in a:
        if i.name == name1:
            job_title1 = i.job_title
            job_title.append(job_title1)
            company_name1 = i.company_name
            company_name.append(company_name1)
    apply = zip(job_title, company_name)
    return render(request, 'applies.html', {'apply': apply})


def regcc(request):
    a = JobApplication.objects.all()
    company_name = []
    email = []
    id = []

    for i in a:
        cname1 = i.company_name
        company_name.append(cname1)
        eml1 = i.email
        email.append(eml1)
        id1 = i.id
        id.append(id1)
    reg = zip(company_name, email, id)
    return render(request, 'regc.html', {'reg': reg})


def send(request, id):
    if request.method == 'POST':
        a = contactform(request.POST)
        if a.is_valid():
            name = a.cleaned_data['name']
            email = a.cleaned_data['email']
            subject = a.cleaned_data['subject']
            msg = a.cleaned_data['message']
            send_mail(subject, msg, EMAIL_HOST_USER, [email], fail_silently=False)
            return HttpResponse('MAIL SENT SUCCESSFULLY')
        else:
            return HttpResponse('NOT VALID')
    b = applyyjob.objects.get(id=id)
    return render(request, 'sendmail.html', {'b': b})
