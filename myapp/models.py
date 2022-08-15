from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.CharField(primary_key=True,unique=True,null=False,blank=False,max_length=30)
    name = models.CharField(max_length=100, null=False, blank=False)
    pan = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self) -> str:
        return self.id



class Product(models.Model):
    name = models.CharField(primary_key=True,unique=True,null=False,blank=False,max_length=30)
    description = models.CharField(max_length=2000)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self) -> str:
        return self.name



class Subscription(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete= models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_user_subscriber = models.IntegerField(default=0)
