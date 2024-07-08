from django.shortcuts import render,redirect
from _datetime import datetime
from .models import *
from django.contrib import messages
# Create your views here.


def indexpage(request):
    current_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S %B %A')
    context={
        'current_date':current_date
    }
    return render(request,"index.html",context)


def submitdata(request):
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    email=request.POST.get('email')
    password=request.POST.get('password')
    phone=request.POST.get('phone')
    storedata=User_table(First_name=fname,Last_name=lname,Email=email,Password=password,Phone=phone)
    messages.success(request,"Data Submitted Successfully....")
    storedata.save()
    return redirect("/")



def submissiondatapage(request):
    submissions=User_table.objects.all()
    context={
        "Data":submissions
    }
    return render(request,"submission.html",context)