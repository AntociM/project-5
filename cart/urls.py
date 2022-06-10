from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<item_id>/', views.adjust_quantity, name='adjust_quantity'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart')
]
