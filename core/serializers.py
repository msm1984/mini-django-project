from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer, TokenCreateSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


    def create(self, validated_data):
        
        user = super().create(validated_data)
        user.is_active = False
        user.save()
        return user

    
class myUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name']


