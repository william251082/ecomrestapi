from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ecom.models import Product, Owner
from ecom.api.serializers import ProductSerializer, OwnerSerializer


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


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": {
            "code": 404,
            "message": "Product not found!"
        }}, status=status.HTTP_404_NOT_FOUND)

    # get details of a single product
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # update details of a single product
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single product
    elif request.method == 'DELETE':
        return Response({})
