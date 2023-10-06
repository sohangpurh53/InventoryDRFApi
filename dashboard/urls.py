from django.urls import path, include, re_path
from django.conf import settings
from dashboard.views import (ProductDisplayView, PurchaseDispalyView, 
                             OrderItemDispalyView, StockDispalyView, 
                             SupplierDispalyView,
                            #  TableOrderItemListView,
                            #  TablePurchaseListView,
                            #  TableStockListView,
                             CategoryDisplayView,
                             CategoryUpdateView,
                             TableListView
                             )



urlpatterns = [
    path('products/list/', ProductDisplayView.as_view(), name='product-list'),
    path('purchase/list/', PurchaseDispalyView.as_view(), name='product-list'),
    path('order/list/', OrderItemDispalyView.as_view(), name='product-list'),
    path('stock/list/', StockDispalyView.as_view(), name='stock-list'),
    path('category/list/', CategoryDisplayView.as_view(), name='category-list'),
    path('supplier/list/', SupplierDispalyView.as_view(), name='supplier-list'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='supplier-list'),

    #for tables only
    path('list/table/', TableListView.as_view(), name='orderitem-list'),
    # path('table/stock/list/', TableStockListView.as_view(), name='stock-list'),
    # path('table/purchase/list/', TablePurchaseListView.as_view(), name='purchase-list'),
  
]
