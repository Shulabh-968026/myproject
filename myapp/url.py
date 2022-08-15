
from django.urls import path
from . import views

urlpatterns = [
    path("",views.subscription_list, name= "subscrption"),
    path("<int:pk>/",views.subscription_detail, name= "subscrption_details"),
    path("customer/",views.customer_list, name= "customer"),
    path("product/",views.product_list, name= "product"),
    path("subscription_check/<int:customer_id>/<str:product_name>/", 
        views.subscription_check, name= "subscription_check"),
]