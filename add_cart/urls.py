from django.urls import path
from . import views

urlpatterns=[
    path('cart_detials',views.cart_details,name='cart_details'),
    path('addcart/<int:product_id>/',views.add_cart,name='addcart'),
    path('cart_decrement/<int:product_id>/',views.min_cart,name='cart_decrement'),
    path('remove/<int:product_id>/',views.cart_delete,name='remove')

]