from django.urls import path, include, re_path
from django.conf import settings
from dashboard.views import (ProductDisplayView,  ProductUpdateView, ProductDeleteView,
                             PurchaseDispalyView, PurchaseUpdateView,PurchaseDeleteView,
                             OrderItemDispalyView, UpdateOrderItemView,
                             StockDispalyView, StockUpdateView,
                             CustomerView, CustomerDeleteView,CustomerUpdateView,
                             SupplierDispalyView,SupplierUpdateView,
                             CategoryDisplayView, CategoryUpdateView, CategoryDeleteView,
                             TableListView,
                             )



urlpatterns = [
    path('products/list/', ProductDisplayView.as_view(), name='product-list'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
      path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-update'),

    path('purchase/list/', PurchaseDispalyView.as_view(), name='purchase-list'),
    path('purchase/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase-update'),
    path('purchase/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase-delete'),
  

    path('order/list/', OrderItemDispalyView.as_view(), name='order-list'), 
    path('orderitem/<int:pk>/update/', UpdateOrderItemView.as_view(), name='orderitem-update'),

    path('stock/list/', StockDispalyView.as_view(), name='stock-list'),
    path('stock/<int:pk>/update/', StockUpdateView.as_view(), name='stock-update'),

    path('category/list/', CategoryDisplayView.as_view(), name='category-list'), 
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-udpate'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete-category'),

    path('supplier/list/', SupplierDispalyView.as_view(), name='supplier-list'),
    path('supplier/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier-list'),


    path('customer/list/', CustomerView.as_view(), name='customer-list'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
   

    #for tables only
    path('list/table/', TableListView.as_view(), name='orderitem-list'),
    
]
