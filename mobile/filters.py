# filters.py
from django_filters import rest_framework as filters
from .models import *

class MobileFilter(filters.FilterSet):
    Nationality = filters.CharFilter(lookup_expr='icontains')
    Name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = MoblieInfo
        fields = ['Nationality', 'Name']


    def get_queryset(self):
        # Retrieve column names from query parameters
        column1 = self.request.query_params.get('column1')
        column2 = self.request.query_params.get('column2')
        
        # Get the initial queryset with filters, search, and ordering applied
        queryset = super().get_queryset()
        
        # Apply the dynamic column comparison if both columns are provided
        if column1 and column2:
            # Validate that the provided columns exist in the model
            if not hasattr(YourModel, column1) or not hasattr(YourModel, column2):
                raise ValidationError("Invalid column names provided for comparison.")
            queryset = queryset.filter(**{f"{column1}": F(column2)})
        
        return queryset