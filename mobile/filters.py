# filters.py
from django_filters import rest_framework as filters
from .models import *

class MobileFilter(filters.FilterSet):
    nationality = filters.CharFilter(lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = MobileInfo
        fields = ['nationality', 'name']


    