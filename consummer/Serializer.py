from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
class Image_serializers(serializers.ModelSerializer):
    class Meta:
        model=Image_upload
        fields="__all__"
class User_serializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields="__all__"