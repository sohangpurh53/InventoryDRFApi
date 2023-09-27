from django.urls import path, include, re_path
from django.conf import settings
from dashboard.views import (ProductDisplayView, PurchaseDispalyView, OrderItemDispalyView)



urlpatterns = [
    path('products/list/', ProductDisplayView.as_view(), name='product-list'),
    path('purchase/list/', PurchaseDispalyView.as_view(), name='product-list'),
    path('order/list/', OrderItemDispalyView.as_view(), name='product-list'),
]
