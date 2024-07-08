from django.urls import path
from . import views
from .models import  *

urlpatterns=[
    path('',views.indexpage),
    path('submitdata',views.submitdata,name="submitdata"),
    path('submissiondatapage',views.submissiondatapage,name="submissiondatapage")
]