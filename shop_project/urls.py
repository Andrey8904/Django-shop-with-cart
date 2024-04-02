from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('shop.urls', namespace='shop')),
    path('', include('reg_log.urls', namespace='reg_log')),
    path('', include('favorites.urls', namespace='favorites')),
    path('', include('product_review.urls', namespace='product_review')),
    path('', include('restore_password.urls', namespace='restore_password')),
    path('', include('rating.urls', namespace='rating')),

]
admin.site.site_header = 'Моя админка'
admin.site.index_title = 'Данные магазина'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
