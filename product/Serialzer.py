from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Food_type
        fields="__all__"
