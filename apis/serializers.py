from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class TypographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Typography
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id', 'book', 'amount', 'total_price']
    def get_total_price(self, obj):
        return obj.book.price * obj.amount

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','name', 'author', 'category', 'description', 'typography')
    # author = AuthorSerializer()
    # typography = TypographySerializer()
    # category = CategorySerializer()



