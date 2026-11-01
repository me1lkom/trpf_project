from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from offers.models import Offer


def offer_list(request: HttpRequest) -> HttpResponse:
    offers: QuerySet[Offer] = (
        Offer.objects
        .select_related('product', 'supplier')
        .order_by('id')
    )

    context: dict[str, QuerySet[Offer]] = {
        'offers': offers,
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
