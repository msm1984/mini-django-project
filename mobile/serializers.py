from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from logging import raiseExceptions



class InformationSerializer(serializers.ModelSerializer):
    checkExist = serializers.SerializerMethodField()
    
    class Meta:
        model = MoblieInfo
        fields = ["Name", "Nationality", "Type", "price", "color", 
                  "screenSize", "checkExist", "country"]

    def get_checkExist(self,obj):
        return obj.get_checkExist_display()


    