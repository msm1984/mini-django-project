from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *



class InformationSerializer(serializers.ModelSerializer):
    check_exist = serializers.SerializerMethodField()
    
    class Meta:
        model = MobileInfo
        fields = ["name", "nationality", "mobile_type", "price", "color", 
                  "screen_size", "check_exist", "country", "count"]

    def get_check_exist(self,obj):
        return obj.get_check_exist_display()


    def update(self, instance, validated_data):
        new_type = validated_data.get('mobile_type', instance.mobile_type)
        
        if new_type != instance.mobile_type:
            if MobileInfo.objects.filter(mobile_type=new_type).exists():
                raise ValidationError({"type": "Mobile info with this mobile type already exists."})
        
        return super().update(instance, validated_data)


    