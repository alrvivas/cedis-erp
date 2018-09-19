#encoding:utf-8
import uuid
from django.db import models
from django.contrib.auth.models import User
from person.models import Employee,Client
from product.models import Product

class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Payment_Status(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True,null=True, blank=True,verbose_name=('Slug'))

    def __str__(self):
        return self.name

class Shipping_Status(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True,null=True, blank=True,verbose_name=('Slug'))

    def __str__(self):
        return self.name

class Payment_Type(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True,null=True, blank=True,verbose_name=('Slug'))

    def __str__(self):
        return self.name

class Order(AbstractModel):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=True, blank=True)
    payment_status = models.ForeignKey(Payment_Status,on_delete=models.CASCADE, null=True, blank=True)
    shipping_status = models.ForeignKey(Shipping_Status,on_delete=models.CASCADE,null=True,blank=True)
    payment_type = models.ForeignKey(Payment_Type,on_delete=models.CASCADE,null=True,blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total_weight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    observacion = models.TextField(null=True,blank=True)

    def __str__(self): 
        return self.client.name

class Deposit_Balance(AbstractModel):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True, blank=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    def __str__(self): 
        return self.order.client.name