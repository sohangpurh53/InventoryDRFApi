from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models.py


class Supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    address = models.TextField()
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    address = models.TextField()
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.full_name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('successful', 'Successful'),
        ('pending', 'Pending'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.customer.full_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.PROTECT) 
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        stock, created = Stock.objects.get_or_create(product=self.product)
        stock.decrease_quantity(self.quantity)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        stock, created = Stock.objects.get_or_create(product=self.product)
        stock.decrease_quantity(self.quantity)

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT) 
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        stock, created = Stock.objects.get_or_create(product=self.product)
        stock.increase_quantity(self.quantity)
    def __str__(self):
        return self.product.name

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        stock = Stock.objects.get(product=self.product)
        stock.decrease_quantity(self.quantity)
    

    def __str__(self):
        return self.product.name
   
class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    

    def increase_quantity(self, amount):
        self.quantity += amount
        self.price = self.product.price * self.quantity  # Update price based on quantity
        self.save()

    def decrease_quantity(self, amount):
        self.quantity -= amount
        self.price = self.product.price * self.quantity  # Update price based on quantity
        self.save()
    
    def __str__(self):
        return self.product.name
 
  
    
    
    