from django.contrib import admin
from .models import Customer, Product, Subscription
# Register your models here.

admin.site.register([Customer, Product, Subscription])
