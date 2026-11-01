from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet, Count
from suppliers.models import Supplier
from products.models import Product
from offers.models import Offer
from users.models import User


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'homepage/index.html')


def statistics(request: HttpRequest) -> HttpResponse:

    offers_to_suppliers: QuerySet[Supplier] = (
        Supplier.objects
        .annotate(count_offers=Count('offers'))
        .order_by('id')
    )

    offers_to_products: QuerySet[Product] = (
        Product.objects
        .annotate(count_offers=Count('offers'))
        .order_by('id')
    )

    count_offers: int = Offer.objects.count()

    count_suppliers: int = Supplier.objects.count()

    count_users: int = User.objects.count()

    count_products: int = Product.objects.count()

    context: dict[str, int | QuerySet[Product] | QuerySet[Supplier]] = {
        'offers_to_suppliers': offers_to_suppliers,
        'offers_to_products': offers_to_products,
        'count_offers': count_offers,
        'count_suppliers': count_suppliers,
        'count_users': count_users,
        'count_products': count_products
    }

    return render(request, 'homepage/statistics.html', context)


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(
        request,
        '404.html',
        status=404,
    )
