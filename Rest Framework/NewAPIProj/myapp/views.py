from django.shortcuts import render
from .serailizers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all() #ORM
    serial=studserial(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=studserial(stid)
    return Response(data=serial.data)


@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=studserial(stid)
        return Response(data=serial.data)

    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serail=studserial(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=studserial(stid)
        return Response(data=serial.data)
    if request.method=='PUT':
        serail=studserial(data=request.data, instance=stid)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

