from django.urls import path
from . import views


app_name = 'reg_log'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('activate/', views.Activate.as_view(), name='activate'),
    path('cant_enter/', views.CantEnter.as_view(), name='cant_enter'),
    path('other_activate/', views.OtherActivate.as_view(), name='other_activate'),
    path('other_activate_code/', views.OtherActivateCode.as_view(), name='other_activate_code'),

]