from django.urls import path
from . import views


app_name = 'restore'

urlpatterns = [
    path('restore_password/', views.restore, name='restore_password'),
    path('restore_code/', views.restore_code, name='restore_code'),
    path('new_password/', views.new_password, name='new_password'),

]