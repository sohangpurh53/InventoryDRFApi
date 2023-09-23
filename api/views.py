from django.shortcuts import render
from rest_framework import generics
from api.models import Supplier, Customer, Category, Product, Order, OrderItem, Purchase, Stock
from api.serializers import (SupplierSerializer, CustomerSerializer, 
                             ProductSerializer, CategorySerializer,
                               PurchaseSerializer, listPurchaseSerializer,
                               listStockSerializer, listOrderSerializer,
                                 listOrderItemSerializer, createOrderItemSerializer, updatePurchaseSerializer)
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class SupplierCreateView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminUser]

class SupplierListView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

   

class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

class CustomerView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDeleteView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class PurchaseCreateView(generics.CreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminUser]

class PurchaseListView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = listPurchaseSerializer

class PurchaseUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = listStockSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = listOrderSerializer


class OrderItemListView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = listOrderItemSerializer

class CreateOrderItemView(generics.CreateAPIView):
    serializer_class = createOrderItemSerializer





