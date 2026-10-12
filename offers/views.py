from django.http import HttpResponse

from homepage.views import page
from storage import load_offers
from storage import load_products
from storage import load_suppliers
from models.offers import get_offer_by_id


def offer_list(request):
    items = ''
    products = load_products('data/products.json')
    suppliers = load_suppliers('data/suppliers.json')

    for offer in load_offers('data/offers.json', products, suppliers):
        items += (
            '<li class="list-group-item">'
            f'<a href="/offers/{offer.id}/">'
            f'{offer.product.name} — {offer.supplier.name}'
            '</a>'
            '</li>'
        )

    content = f"""
    <h1>Предложения</h1>
    <ul class="list-group">{items}</ul>
    """

    return HttpResponse(page('Список предложений', content))


def offer_details(request, offer_id):
    products = load_products('data/products.json')
    suppliers = load_suppliers('data/suppliers.json')

    offers = load_offers('data/offers.json', products, suppliers)
    offer = get_offer_by_id(offers, offer_id)

    if offer is None:
        content = """
        <h1 class="text-danger">Предложение не найдено</h1>
        <a href="/offers/" class="btn btn-outline-secondary">
            ← к списку предложений
        </a>
        """

        return HttpResponse(page('Предложение не найдено', content),
                            status=404)

    content = f"""
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{offer.product.name} —
                    {offer.supplier.name}</h5>
                <p class="card-text">
                    <h6>Предложение</h6>
                    <ul class="list-group">
                        <li class="list-group-item">
                            <strong>ID:</strong>
                            {offer.id}
                        </li>
                        <li class="list-group-item">
                            <strong>Цена:</strong>
                            {offer.price}
                        </li>
                        <li class="list-group-item">
                            <strong>Минимальное количество:</strong>
                            {offer.min_lots}
                        </li>
                        <li class="list-group-item">
                            <strong>Срок доставки:</strong>
                            {offer.delivery_time_days}
                        </li>
                    </ul>
                </p>
                <p class="card-text">
                    <h6>Товар</h6>
                    <ul class="list-group">
                        <li class="list-group-item">
                            <strong>Название товара:</strong>
                            {offer.product.name}
                        </li>
                        <li class="list-group-item">
                            <strong>Описание:</strong>
                            {offer.product.description}
                        </li>
                        <li class="list-group-item">
                            <strong>Страна производства:</strong>
                            {offer.product.country}
                        </li>
                    </ul>
                </p>
                <p class="card-text">
                    <h6>Поставщик</h6>
                    <ul class="list-group">
                        <li class="list-group-item">
                            <strong>Название поставщика:</strong>
                            {offer.supplier.name}
                        </li>
                        <li class="list-group-item">
                            <strong>ИНН:</strong>
                            {offer.supplier.inn}
                        </li>
                        <li class="list-group-item">
                            <strong>Номер:</strong>
                            {offer.supplier.phone}
                        </li>
                        <li class="list-group-item">
                            <strong>Email:</strong>
                            {offer.supplier.email}
                        </li>
                    </ul>
                </p>
                <a href="/offers/" class="btn btn-outline-secondary">
                    ← к списку предложений
                </a>
            </div>
        </div>
    """

    return HttpResponse(page(offer.product.name, content))
