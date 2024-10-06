from django.http import JsonResponse
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