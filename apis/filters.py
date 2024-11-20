from .serializers import *
from .models import *
class BookFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte') 
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['category', 'min_price', 'max_price']