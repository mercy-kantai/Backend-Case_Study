from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_id = models.PositiveSmallIntegerField()
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField()
    
    

    def __str__(self):
        return f"{self.first_name}"