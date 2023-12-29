from django.shortcuts import render
from .forms import *


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