from django.shortcuts import render, redirect, get_object_or_404
from .models import Favorites
from shop.models import Product


def add_to_favorites(request, product_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        favorite_exist = Favorites.objects.filter(user_id=user_id, product_id=product_id).exists()
        if not favorite_exist:
            favorite = Favorites(
                user_id=user_id,
                product_id=product_id
            )
            favorite.save()
        product = Product.objects.get(pk=product_id)
        product_slug = product.slug
        return redirect('shop:product_detail', product_slug=product_slug)

    return redirect('reg_log:login')


def remove_favorite(request, product_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        Favorites.objects.filter(user_id=user_id, product_id=product_id).delete()
        return redirect('reg_log:dashboard')




