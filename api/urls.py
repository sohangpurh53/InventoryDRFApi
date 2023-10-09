from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (SupplierCreateView, CustomerCreateView, 
 ProductCreateView,
PurchaseCreateView, CategoryCreateView,ProductListView,
SupplierListView, CategoryListView,PurchaseListView,
StockListView, OrderListView, OrderItemListView, 
CreateOrderItemView)


urlpatterns = [
    path('supplier/create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('purchase/create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    
    path('stocks/', StockListView.as_view(), name='stock-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order-item/', OrderItemListView.as_view(), name='order-item-list'),
    path('order-item/create/', CreateOrderItemView.as_view(), name='order-item-create'),
  

    
 
]