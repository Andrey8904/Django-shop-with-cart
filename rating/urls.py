from django.urls import path
from . import views


app_name = 'rating'

urlpatterns = [
    path('add_rating/<int:product_id>/<int:rating_value>', views.add_rating, name='add_rating'),

]