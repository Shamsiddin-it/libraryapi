from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('book/', BookListView.as_view(), name='book-list'),
    path('author/', AuthorListView.as_view(), name='author-list'),
    path('typography/', TypographyListView.as_view(), name='typography-list'),
    path('order/', OrderListView.as_view(), name='order-list'),
]