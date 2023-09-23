from django.contrib import admin
from api.models import Supplier, Customer, Category, Product, Order, OrderItem, Purchase, Stock

admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Purchase)
admin.site.register(Stock)