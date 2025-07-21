from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('browse/', views.browse, name='browse'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('shgs/', views.shg_list, name='shg_list'),
    path('shg/<int:pk>/', views.shg_detail, name='shg_detail'),
    path('pickles/', views.pickle_list, name='pickle_list'),

]

