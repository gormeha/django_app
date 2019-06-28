from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    warehouse = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.name + " -> Location : " + self.warehouse


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(1000), MinValueValidator(0)])
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    interested_in = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name + " -> Stock : " + str(self.stock)

    def refill(self):
        self.stock = self.stock + 100
        return self.stock


class Client(User):
    image = models.ImageField(upload_to="profile", blank=True)
    PROVINCE_CHOICES = [('AB', 'Alberta'), ('MB', 'Manitoba'), ('ON', 'Ontario'), ('QC', 'Quebec')]
    company = models.CharField(max_length=50, null=True, blank=True)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    interested_in = models.ManyToManyField(Category)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Order(models.Model):
    ORDER_STATUS = [(0, 'Order Cancelled'), (1, 'Order Placed'), (2, 'Order Shipped'), (3, 'Order Delivered')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    num_units = models.PositiveIntegerField(default=100)
    order_status = models.IntegerField(choices=ORDER_STATUS, default=1)
    status_date = models.DateField(default=timezone.now)

    def total_cost(self):
        return self.product.price * self.num_units

    def __str__(self):
        return 'Order No: ' + str(self.id) + " by " + str(self.client) + " -> Total Amount: " + str(self.total_cost())
