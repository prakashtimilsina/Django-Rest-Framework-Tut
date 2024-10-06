from django.http import JsonResponse
from api.serializers import ProductSerializer
from api.models import Product


## Function based Views

def product_list(request):
    products = Product.objects.all()
    serilizer = ProductSerializer(products, many=True)
    return JsonResponse({
        'data': serilizer.data
    })