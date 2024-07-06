from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.PositiveSmallIntegerField()
    product_name = models.CharField(max_length= 20)
    product_description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name}"