from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_detail/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('products_in_cat/<int:product_cat>/', views.products_in_cat, name='products_in_cat'),
    path('product_search/', views.product_search, name='product_search'),

]