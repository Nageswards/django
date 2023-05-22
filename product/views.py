
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . Serialzer import *
from .models import*
from django.db import models
@api_view(["POST"])
def login(request):
    data=request.data
    if request.method=="POST":
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
@api_view(["POST"])
def category(request):
    data=request.data
    if request.method=="POST":
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=201)
