from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


from storage import load_offers
from storage import load_products
from storage import load_suppliers
from models.offers import Offer, get_offer_by_id


def offer_list(request: HttpRequest) -> HttpResponse:
    products = load_products('data/products.json')
    suppliers = load_suppliers('data/suppliers.json')

    offers = load_offers('data/offers.json', products, suppliers)

    context: dict[str, list[Offer]] = {
        'offers': offers
    }

    return render(request, "offers/offer_list.html", context)


def offer_details(request: HttpRequest, offer_id: int) -> HttpResponse:
    products = load_products('data/products.json')
    suppliers = load_suppliers('data/suppliers.json')

    offers = load_offers('data/offers.json', products, suppliers)
    offer = get_offer_by_id(offers, offer_id)

    context: dict[str, Offer | None] = {
        'offer': offer
    }

    return render(
        request,
        "offers/offer_detail.html",
        context,
        status=404 if offer is None else 200
    )
