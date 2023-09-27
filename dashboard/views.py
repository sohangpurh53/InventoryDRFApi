from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from api.models import Supplier, Customer, Category, Product, Order, OrderItem, Purchase, Stock
from api.serializers import (SupplierSerializer, CustomerSerializer, 
                             ProductSerializer, CategorySerializer,
                               PurchaseSerializer, listPurchaseSerializer,
                               listStockSerializer, listOrderSerializer,
                                 listOrderItemSerializer, createOrderItemSerializer, updatePurchaseSerializer)
# Create your views here.
#dashboard view separately
class CustomProductPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductDisplayView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomProductPageNumberPagination



class SupplierDispalyView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CustomerView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CategoryDispalyView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
  

class PurchaseDispalyView(ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = listPurchaseSerializer
    pagination_class = CustomPageNumberPagination


class StockDispalyView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = listStockSerializer

class OrderDispalyView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = listOrderSerializer


class OrderItemDispalyView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = listOrderItemSerializer
    pagination_class = CustomPageNumberPagination

