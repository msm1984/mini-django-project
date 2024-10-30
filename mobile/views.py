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


    queryset = MoblieInfo.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MobileFilter

    search_fields = ['Nationality', 'Name']

    

    def get_queryset(self):
        # Retrieve column names from query parameters
        column1 = self.request.query_params.get('column1')
        column2 = self.request.query_params.get('column2')
        
        # Get the initial queryset with filters, search, and ordering applied
        queryset = super().get_queryset()
        
        # Apply the dynamic column comparison if both columns are provided
        if column1 and column2:
            # Validate that the provided columns exist in the model
            if not hasattr(MoblieInfo, column1) or not hasattr(MoblieInfo, column2):
                raise ValidationError("Invalid column names provided for comparison.")
            queryset = queryset.filter(**{f"{column1}": F(column2)})
        
        return queryset
