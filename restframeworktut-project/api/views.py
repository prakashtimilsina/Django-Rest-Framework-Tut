from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer
from api.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response


## Function based Views
# def product_list(request):
#     products = Product.objects.all()
#     serilizer = ProductSerializer(products, many=True)
#     return JsonResponse({
#         'data': serilizer.data
#     })


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serilizer = ProductSerializer(products, many=True)
    return Response(serilizer.data)

@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serilizer = ProductSerializer(product)
    return Response(serilizer.data)