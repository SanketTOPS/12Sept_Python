from django.shortcuts import render
from .models import *
from .serailizers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def getall(request):
    data=studinfo.objects.all()
    serial=studserializers(data,many=True)
    return Response(data=serial.data)





