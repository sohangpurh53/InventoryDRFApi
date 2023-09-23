from django.urls import path, include, re_path
from django.conf import settings
from dashboard.views import ProductDisplayView



urlpatterns = [
    path('products/list/', ProductDisplayView.as_view(), name='product-list'),
]
