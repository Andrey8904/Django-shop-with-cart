from django.shortcuts import redirect
from .models import ProductRating
from shop.models import Product

def add_rating(request, product_id, rating_value):
    if 'user_id' not in request.session:
        return redirect('reg_log:login')

    check_rating = ProductRating.objects.filter(user_id=request.session['user_id'], product_id=product_id).first()
    if not check_rating:
        new_rating = ProductRating(
            user_id=request.session['user_id'],
            product_id=product_id,
            rating_value=rating_value
        )
        new_rating.save()

        product = Product.objects.get(pk=product_id)
        return redirect('shop:product_detail', product.slug)

    product = Product.objects.get(pk=product_id)
    return redirect('shop:product_detail', product.slug)
