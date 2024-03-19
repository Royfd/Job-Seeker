from django.urls import path

from jobseeker import views
from .views import *

urlpatterns=[
    path('',homme),
    path('register/',regis),
    path('success/',success),
    path('send/',send_mail_regis),
    path('error/',error),
    path('log/',lo),
    path('verify/<auth_token>',verify),
    path('addjobb/<int:id>',jobapplication),
    path("regg/", reg),
    path("logg/", logins),
    path("edits/<int:id>",edit),
    path('updatess/<int:id>',updates),
    path("logg/",show),
    path("open/<int:id>",openings),
    path('job/<int:id1>/<int:id2>',jobdt),
    path('apply/<int:id1>/<int:id2>',applyy),
    path('applicants/<int:id>',view_applicant),
    path('app/<int:id>',applied),
    path('regc/',regcc),
    path('mail/<int:id>',send)
]
