from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.

def index(request):
    if request.method=='POST': #true
        newdata=studForm(request.POST)
        if newdata.is_valid(): #TRUE
            newdata.save()
            print("Your data has been saved!")
        else:
            print(newdata.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=='POST': #true
        update=updateForm(request.POST,instance=stid)
        if update.is_valid(): #TRUE
            update.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(update.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')

    