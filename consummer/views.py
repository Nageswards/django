from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .Serializer import *
from django.contrib.auth import authenticate,login,logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.views import APIView
@api_view(["GET"])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def User_get(request,id):
    user_data=User.objects.get(id=id)
    
    user_serializers=User_serializers(user_data)
    return Response(user_serializers.data)
@api_view(["POST","GET"])
def user_based(request):
    data=request.data
    if request.method=="GET":
        user_data=User.objects.all()
        user_serializers=User_serializers(user_data,many=True)
        return Response(user_serializers.data)
    elif request.method=="POST":
        if authenticate(username=data["user"],password=data["pass"]):
            user_data=User.objects.all()
            user_serializers=User_serializers(user_data,many=True)
            return Response(user_serializers.data)

@api_view(["POST"])
def login(request):
    
    data=request.data
    if request.method=="POST":
        user=authenticate(username=data["user"],password=data["pass"])
        if user:
            return Response("User login")
        else:
            return Response("test")
        
class Home(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = Image_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)