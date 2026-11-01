from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from offers.models import Offer
from suppliers.models import Supplier
from django.core.paginator import Paginator


def offer_list(request: HttpRequest) -> HttpResponse:

    order_by = {
        'default': 'id',
        'price': 'price',
        'delivery': 'delivery_time_days',
        'supplier_name': 'supplier__name'
    }

    sort = request.GET.get('sort', 'default')
    sorting = order_by.get(sort, order_by['default'])

   
    offers: QuerySet[Offer] = (
        Offer.objects
        .select_related('product', 'supplier')
        .order_by(sorting)
    )

    suppliers: QuerySet[Supplier]  = Supplier.objects.order_by('name')

    filters: dict[str, str] = {
        'max_price': request.GET.get('max_price', default=''),
        'max_delivery': request.GET.get('max_delivery', default=''),
        'country': request.GET.get('country', default=''),
        'exclude_supplier': request.GET.get('exclude_supplier', default='')
    }
    supplier_selected = 0


    if filters['country'] != '':
        offers = offers.filter(
            product__country__icontains=filters['country']
        )

    if filters['exclude_supplier'].isdigit():
        offers = offers.exclude(
            supplier_id=int(filters['exclude_supplier'])
        )
        supplier_selected = int(filters['exclude_supplier'])

    if filters['max_price'].replace('.', '', 1).isdigit():
        max_price = float(filters['max_price'])
        if max_price > 0:
            offers = offers.filter(price__lte=max_price)

    if filters['max_delivery'].isdigit():
        max_delivery = int(filters['max_delivery'])
        if max_delivery > 0:
            offers = offers.filter(delivery_time_days__lte=max_delivery)

    paginator = Paginator(offers, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'offers': page_obj,
        'page_obj': page_obj,
        'suppliers': suppliers,
        'sort': sort,
        'supplier_selected': supplier_selected
    }

    return render(request, "offers/offer_list.html", context)


def offer_details(request: HttpRequest, offer_id: int) -> HttpResponse:
    offer: Offer = get_object_or_404(
        Offer.objects.select_related(
            'product',
            'supplier',
            'product__buyer_record__user',
            'product__buyer_record__supplier'
        ),
        pk=offer_id
    )

    buyer = getattr(offer.product, 'buyer_record', None)

    if buyer is None:
        buyers_name = None
        buyers_type = None
    elif buyer.user_id is not None:
        buyers_name = buyer.user.name
        buyers_type = 'Физ лицо'
    else:
        buyers_name = buyer.supplier.name
        buyers_type = 'Организация'

    context = {
        'offer': offer,
        'buyers_name': buyers_name,
        'buyers_type': buyers_type
    }

    return render(
        request,
        "offers/offer_detail.html",
        context
    )
