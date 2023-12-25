from django.shortcuts import render
import random

# Create your views here.

def index(request):
    name="Ashok"
    return render(request,'index.html',{'nm':name})

def abbout(request):
    num=random.randint(1111,9999)
    return render(request,'about.html',{'num':num})

def contact(request):
    return render(request,'contact.html')