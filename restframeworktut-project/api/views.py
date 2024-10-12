from django.shortcuts import get_object_or_404, render
from api.serializers import ProductSerializer, OrderItemSerializer, OrderSerializer
from api.models import Product, OrderItem, Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics




# HOME page only
def home(request):
    return render(request, 'api/home.html')

## Function based Views
# def product_list(request):
#     products = Product.objects.all()
#     serilizer = ProductSerializer(products, many=True)
#     return JsonResponse({
#         'data': serilizer.data
#     })

#Class based GET
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Function based GET
    # @api_view(['GET'])
    # def product_list(request):
    #     products = Product.objects.all()
    #     serilizer = ProductSerializer(products, many=True)
    #     return Response(serilizer.data)

# class based view
class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Function based GET
    # @api_view(['GET'])
    # def product_detail(request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     serilizer = ProductSerializer(product)
    #     return Response(serilizer.data)

# class based View
class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Function based GET
    # @api_view(['GET'])
    # def order_list(request):
    #     orders = Order.objects.all()
    #     serilizer = OrderSerializer(orders, many=True)
    #     return Response(serilizer.data)