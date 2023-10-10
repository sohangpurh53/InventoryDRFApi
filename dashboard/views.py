from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from api.models import Supplier, Customer, Category, Product, Order, OrderItem, Purchase, Stock
from api.serializers import (SupplierSerializer, CustomerSerializer, 
                             ProductSerializer, CategorySerializer,
                               PurchaseSerializer, listPurchaseSerializer,
                               listStockSerializer, listOrderSerializer,
                                 listOrderItemSerializer, createOrderItemSerializer,updateOrderItemSerializer,
                                   updatePurchaseSerializer)
from rest_framework.permissions  import IsAdminUser
from rest_framework.response import Response

# Create your views here.


                                     #Dashboard View Separately..

# Custom Permisson Classes For Pagination
class CustomProductPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomCategoryPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



#Product listing and CURD
class ProductDisplayView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomProductPageNumberPagination

class ProductUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]

class ProductDeleteView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]


#Supplier listing and CURD
class SupplierDispalyView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminUser]

class SupplierUpdateView(RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminUser]


#Customer listing and CURD
class CustomerView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

class CustomerDeleteView(RetrieveDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

class CustomerUpdateView(RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

  

#Purchase listing and CURD
class PurchaseDispalyView(ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = listPurchaseSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAdminUser]

class PurchaseUpdateView(RetrieveUpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminUser]

class PurchaseDeleteView(RetrieveDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminUser]


#Stock listing and CURD
class StockDispalyView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = listStockSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPageNumberPagination

class StockUpdateView(RetrieveUpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = listStockSerializer
    permission_classes = [IsAdminUser]




   


#Order listing and CURD
class OrderDispalyView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = listOrderSerializer
    permission_classes = [IsAdminUser]


#OrderItem listing and CURD
class OrderItemDispalyView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = listOrderItemSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAdminUser]

class UpdateOrderItemView(RetrieveUpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = updateOrderItemSerializer
    permission_classes = [IsAdminUser]



#Customer listing and CURD
class CategoryDisplayView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomCategoryPageNumberPagination
    permission_classes = [IsAdminUser]



class CategoryUpdateView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryDeleteView(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


#table view for all stocks including purchase and order
class TableListView(ListAPIView):
    serializer_class_order_item = listOrderItemSerializer
    serializer_class_purchase = listPurchaseSerializer
    serializer_class_stock = listStockSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        order_item_data = OrderItem.objects.all()
        purchase_data = Purchase.objects.all()
        stock_data = Stock.objects.all()

        return {
            'order_item_data': order_item_data,
            'purchase_data': purchase_data,
            'stock_data': stock_data
        }

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()

        order_item_serializer = self.serializer_class_order_item(data['order_item_data'], many=True)
        purchase_serializer = self.serializer_class_purchase(data['purchase_data'], many=True)
        stock_serializer = self.serializer_class_stock(data['stock_data'], many=True)

        return Response({
            'order_item_data': order_item_serializer.data,
            'purchase_data': purchase_serializer.data,
            'stock_data': stock_serializer.data
        })