from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
 #   path('products/', views.product_list), # Function based view
    path('products/', views.ProductListApiView.as_view()), # class based view
  #  path('products/<int:pk>/', views.product_detail),
    path('products/<int:pk>/', views.ProductDetailApiView.as_view()),
  #  path('orders/', views.order_list),
    path('orders/', views.OrderListApiView.as_view()),
]
