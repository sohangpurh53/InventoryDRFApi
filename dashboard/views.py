from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from api.models import Supplier, Customer, Category, Product, Order, OrderItem, Purchase, Stock
from api.serializers import ProductSerializer
# Create your views here.
#dashboard view separately
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductDisplayView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination