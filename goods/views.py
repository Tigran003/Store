from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from  goods.models import Products
from  goods.utils import  search_q


def catalog(request, category_slug=None) -> HttpResponse:
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all-products':
        goods = Products.objects.all()

    elif category_slug != 'all-category':
        goods = Products.objects.all().filter(category__slug=category_slug)

    elif query:
        goods = search_q(query)

    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Catalog',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug) -> HttpResponse:
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
