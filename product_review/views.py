from django.shortcuts import redirect
from .models import AddReview
from shop.models import Product

def add_review(request, product_id):
    if 'user_id' in request.session and request.method == 'POST':
        user_id = request.session['user_id']
        product_review = request.POST['product_review']
        new_review = AddReview(user_id=user_id, product_id=product_id, text_review=product_review)
        new_review.save()
        product = Product.objects.get(pk=product_id)
        product_slug = product.slug
        return redirect('shop:product_detail', product_slug=product_slug)
    return redirect('reg_log:login')


def remove_review(request, review_id):
    if 'user_id' in request.session and request.method == 'POST':
        user_id = request.session['user_id']
        # запрос на получение отзыва из таблицы AddReview
        get_review = AddReview.objects.get(pk=review_id)

        product_id = get_review.product_id
        product = Product.objects.get(pk=product_id)
        product_slug = product.slug

        if user_id == get_review.user_id:
            # udalenie_otziva_iz_bd
            AddReview.objects.get(pk=review_id).delete()
            return redirect('shop:product_detail', product_slug=product_slug)

        return redirect('shop:product_detail', product_slug=product_slug)





