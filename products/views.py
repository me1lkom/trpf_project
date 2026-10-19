from django.shortcuts import render

from storage import load_products
from models.products import get_product_by_id


def product_list(request):
    products = load_products('data/products.json')

    context = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)


def product_details(request, product_id):
    products = load_products('data/products.json')
    product = get_product_by_id(products, product_id)

    context = {
        'product': product,
    }

    return render(
        request,
        'products/product_detail.html',
        context,
        status=404 if product is None else 200,
    )
