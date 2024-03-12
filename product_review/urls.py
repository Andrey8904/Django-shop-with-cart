from django.urls import path
from . import views


app_name = 'product_review'

urlpatterns = [
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('remove_review/<int:review_id>/', views.remove_review, name='remove_review'),

]