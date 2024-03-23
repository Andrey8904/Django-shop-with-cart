from django.shortcuts import render, get_object_or_404
from .models import Product
from reg_log.models import CustomUser
from cart.forms import CartAddProductForm
from product_review.models import AddReview
from rating.models import ProductRating


def index(request):
    products = Product.objects.all()
    if 'user_id' in request.session:
        user = CustomUser.objects.get(pk=request.session['user_id'])
        return render(request, 'shop/index.html', {'products': products, 'user': user})
    return render(request, 'shop/index.html', {'products': products, 'user': None})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)

    cart_product_form = CartAddProductForm()
    get_reviews = AddReview.objects.filter(product_id=product.id)
    get_user_ids = [get_id.user_id for get_id in get_reviews]
    users_reviews = CustomUser.objects.filter(id__in=get_user_ids)

    fact_rating = None
    get_rating = ProductRating.objects.filter(product_id=product.id)

    if get_rating:
        product_ratings = [rating.rating_value for rating in get_rating]
        fact_rating = round((sum(product_ratings) / len(product_ratings)), 1)

    if 'user_id' in request.session:
        return render(request, 'shop/product/detail.html',
                      {'product': product, 'cart_product_form': cart_product_form, 'user': True,
                       'session_user_id': request.session['user_id'],
                       'users_reviews': users_reviews, 'get_reviews': get_reviews, 'fact_rating': fact_rating})

    return render(request, 'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form, 'user': None,
                   'users_reviews': users_reviews, 'get_reviews': get_reviews, 'fact_rating': fact_rating})


def products_in_cat(request, product_cat):
    products = Product.objects.all().filter(category=product_cat)
    if 'user_id' in request.session:
        return render(request, 'shop/product/products_in_category.html', {'products': products, 'user': True})
    return render(request, 'shop/product/products_in_category.html', {'products': products, 'user': None})


def product_search(request):
    if 'query' in request.GET:
        user_input = request.GET['query']
        products = Product.objects.filter(name__icontains=user_input)
    else:
        user_input = request.POST['user_input']
        products = Product.objects.filter(name__icontains=user_input)
    user = True if 'user_id' in request.session else False
    data = {'products': products, 'user': user}
    return render(request, 'shop/product/search_product.html', data)
