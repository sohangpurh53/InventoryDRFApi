from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Supplier, Customer, Category, Product, Order, OrderItem, Purchase, Stock
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Set password as write-only field

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Set and hash the password
        user.save()
        return user

class SupplierSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Supplier
        fields = ['id', 'user', 'address', 'mobile_no']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        supplier = Supplier.objects.create(user=user, **validated_data)
        return supplier

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'full_name','email', 'address', 'mobile_no']

   


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'description', 'image' , 'price', 'supplier']
    
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id','supplier', 'product', 'quantity']

class listPurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Purchase
        fields = ['id','supplier', 'product', 'quantity']

class listStockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Purchase
        fields = ['product', 'quantity',]

class listOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Order
        fields = ['customer', 'order_date', 'order_status']

class listOrderItemSerializer(serializers.ModelSerializer):
    order = listOrderSerializer()
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'order_status', 'order_date']
        
      

class createOrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']

    def create(self, validated_data):
        order_data = validated_data.pop('order')
        order, created = Order.objects.get_or_create(**order_data)
        order_item = OrderItem.objects.create(order=order, **validated_data)
        return order_item


class UpdateProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'description', 'image' , 'price', 'supplier']


class updatePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id','supplier', 'product', 'quantity']