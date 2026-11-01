from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet, Min, Max, Avg
from django.db.models.functions import Round
from products.models import Product
from offers.models import Offer


def product_list(request: HttpRequest) -> HttpResponse:
    products: QuerySet[Product] = Product.objects.all().order_by('id')

    context: dict[str, QuerySet[Product]] = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)


def product_details(request: HttpRequest, product_id: int) -> HttpResponse:
    product: Product = get_object_or_404(
        Product.objects.select_related(
            'buyer_record__user',
            'buyer_record__supplier'
        ),
        pk=product_id
    )

    buyer = getattr(product, 'buyer_record', None)

    if buyer is None:
        buyers_name = None
        buyers_type = None
    elif buyer.user_id is not None:
        buyers_name = buyer.user.name
        buyers_type = 'Физ лицо'
    else:
        buyers_name = buyer.supplier.name
        buyers_type = 'Организация'

    order_by = {
        'default': 'id',
        'price': 'price',
        'delivery': 'delivery_time_days'
    }

    sort = request.GET.get('sort', 'default')
    sorting = order_by.get(sort, order_by['default'])

    print(sort, sorting)

    offers: QuerySet[Offer] = (
        Offer.objects
        .filter(product_id=product_id)
        .select_related('supplier')
        .order_by(sorting)
    )

    price_stat = (
        Offer.objects
        .filter(product_id=product_id)
        .aggregate(
            min_price=Min('price'),
            max_price=Max('price'),
            avg_price=Round(Avg('price'), 2),
        )
    )

    context = {
        'product': product,
        'offers': offers,
        'buyers_name': buyers_name,
        'buyers_type': buyers_type,
        'price_stat': price_stat
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )
