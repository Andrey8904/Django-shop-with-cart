from django.contrib import admin
from .models import AddReview



@admin.register(AddReview)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product_id', 'text_review', 'data_review')
    list_display_links = ('id',)
