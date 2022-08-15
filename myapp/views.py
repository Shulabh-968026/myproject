from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .serializer import CustomerSerializer, ProductSerializer, SubscriptionSerializer
from .models import Customer, Product, Subscription
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def subscription_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def subscription_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Subscription(snippet)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = SubscriptionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def customer_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def subscription_check(request,customer_id, product_name):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        subscription_check = get_object_or_404(Subscription,customer_id=customer_id, product_name= product_name)
        serializer = SubscriptionSerializer(subscription_check)
        return Response(serializer.data)