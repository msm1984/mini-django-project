from django.db.models import F
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .models import *
from .filters import *
from .serializers import *


class InformationViewSet(ModelViewSet):


    queryset = MobileInfo.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MobileFilter

    search_fields = ['nationality', 'name']

    

    def get_queryset(self):
        
        column1 = self.request.query_params.get('column1')
        column2 = self.request.query_params.get('column2')
        
        
        queryset = super().get_queryset()
        
        
        if column1 and column2:
            
            if not hasattr(MobileInfo, column1) or not hasattr(MobileInfo, column2):
                raise ValidationError({"type":"Invalid column names provided for comparison."})
            queryset = queryset.filter(**{f"{column1}": F(column2)})
        
        return queryset
