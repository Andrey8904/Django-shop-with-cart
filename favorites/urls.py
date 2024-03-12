from django.urls import path
from . import views


app_name = 'favorites'

urlpatterns = [
    path('add_to_favorites/<int:product_id>', views.add_to_favorites, name='add_to_favorites'),
    path('remove_favorite/<int:product_id>', views.remove_favorite, name='remove_favorite'),

]