from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from ecom.models import Product, Owner
from ecom.api.serializers import ProductSerializer, OwnerSerializer


@api_view(["GET", "POST"])
def product_list_create_api_view(request):

    if request.method == "GET":
        products = Product.objects.filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_detail_api_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": {
                            "code": 404,
                            "message": "Product not found!"
                        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_products(request):
    # get all products
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    # insert a new record for a product
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'body': request.data.get('body'),
            'location': request.data.get('location'),
            'release_date': request.data.get('release_date'),
            'active': request.data.get('active')
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
