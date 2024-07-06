from django.db import models
from .models import Customers
from .models import Products


# Create your models here.
class Orders(models.Model):
    order_id= models.CharField(max_length= 20)
    customer_id = models.ForeignKey(Customers , on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products , on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places= 2, default= 0)
    

    def __str__(self):
        return f"{self.order_id}"
