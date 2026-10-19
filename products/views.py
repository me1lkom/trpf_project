from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from storage import load_products
from models.products import Product, get_product_by_id


def product_list(request: HttpRequest) -> HttpResponse:
    products = load_products('data/products.json')

    context: dict[str, list[Product]] = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)


def product_details(request: HttpRequest, product_id: int) -> HttpResponse:
    products = load_products('data/products.json')
    product = get_product_by_id(products, product_id)

    context: dict[str, Product | None] = {
        'product': product,
    }

    return render(
        request,
        'products/product_detail.html',
        context,
        status=404 if product is None else 200,
    )
