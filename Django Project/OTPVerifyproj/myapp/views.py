from django.shortcuts import render,redirect
from .forms import *
import requests
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

otp=0
def usersignup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")

            #OTP Sending Code
            global otp
            otp=random.randint(1111,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"KEodGZf5czOn3eCxJPkWAFHQUYtS86Rbmrv1MyuViag4hs7N2DujvzKSw5MN9mRryb3LC4DsIHiWph78","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['mobile']}"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)

            return redirect('otpverify')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def otpverify(request):
    global otp
    msg=""
    print("Your OTP is:",otp)
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("OTP Verify successfully!")
            msg="OTP Verify successfully!"
            return redirect('/')
        else:
            msg="Verification faild...Try again!"
    return render(request,'otpverify.html',{'msg':msg})