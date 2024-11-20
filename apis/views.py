from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Book
from .serializers import *
from .filters import BookFilter
from rest_framework.filters import SearchFilter
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404  

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category', 'name']  
    ordering_fields = ['id', 'category'] 
    filterset_class = BookFilter
    search_fields = ['name', 'description']
    


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']  
    ordering_fields = ['id', 'name'] 

class AuthorListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']  
    ordering_fields = ['id', 'name'] 

class TypographyListView(ListCreateAPIView):
    queryset = Typography.objects.all()
    serializer_class = TypographySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']  
    ordering_fields = ['id', 'name'] 

class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['book', 'amount']  
    ordering_fields = ['id', 'book'] 
    

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_price = sum(order.amount * order.book.price for order in queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'total_price': total_price,
            'orders': serializer.data
        })




    

