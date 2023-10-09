from django.shortcuts import render
from rest_framework import generics
from api.models import Supplier, Customer, Category, Product, Order, OrderItem, Purchase, Stock
from api.serializers import (SupplierSerializer, CustomerSerializer, 
                             ProductSerializer, CategorySerializer,
                               PurchaseSerializer, listPurchaseSerializer,
                               listStockSerializer, listOrderSerializer,
                                 listOrderItemSerializer, createOrderItemSerializer, 
                                 updatePurchaseSerializer, SignInSerializer)
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.authentication import authenticate
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.tokens import TokenError
from rest_framework.permissions import IsAdminUser


# Create your views here.

#supplier create and list
class SupplierCreateView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminUser]
    

class SupplierListView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    

   
#cstomer create and list
class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]




#product create and list
class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

#category create and list
class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    


#purchase create and list
class PurchaseCreateView(generics.CreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminUser]

    

class PurchaseListView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = listPurchaseSerializer





#stock create and list
class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = listStockSerializer



#orders create and list
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = listOrderSerializer


class OrderItemListView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = listOrderItemSerializer

class CreateOrderItemView(generics.CreateAPIView):
    serializer_class = createOrderItemSerializer



class BlacklistRefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'refresh_token required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            RefreshToken(refresh_token).blacklist()
            return Response({'message': 'refresh token blacklisted successfully'}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)