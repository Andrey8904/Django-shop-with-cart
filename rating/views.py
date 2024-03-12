from django.shortcuts import redirect
from .models import ProductRating
from shop.models import Product

def add_rating(request, product_id, rating_value):
    if 'user_id' not in request.session:
        return redirect('reg_log:login')
    product = Product.objects.get(pk=product_id)
    product_slug = product.slug
    user_id = request.session['user_id']
    new_rating = ProductRating(
        user_id=user_id,
        product_id=product_id,
        rating_value=rating_value
    )
    new_rating.save()
    return redirect('shop:detail', product_slug)

