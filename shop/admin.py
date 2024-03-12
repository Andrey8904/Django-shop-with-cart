from django.contrib import admin
from .models import Product
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_img', 'name', 'price', 'stock', 'created')
    list_display_links = ('id', 'show_img', 'name')

    def show_img(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="60"/>'.format(obj.image.url))

    show_img.__name__ = 'Картинка'

