from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Goods_type
        fields="__all__"