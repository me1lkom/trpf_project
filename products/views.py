from django.http import HttpResponse

from homepage.views import page
from storage import load_products
from models.products import get_product_by_id


def product_list(request):
    items = ''

    for product in load_products('data/products.json'):
        items += (
            '<li class="list-group-item">'
            f'<a href="/products/{product.id}/">'
            f'{product.name} — {product.country}'
            '</a>'
            '</li>'
        )

    content = f"""
    <h1>Товары</h1>
    <ul class="list-group">{items}</ul>
    """

    return HttpResponse(page('Список товаров', content))


def product_details(request, product_id):
    products = load_products('data/products.json')

    product = get_product_by_id(products, product_id)

    if product is None:
        content = """
        <h1 class="text-danger">Продукт не найден</h1>
        <a href="/products/" class="btn btn-outline-secondary">
            ← к списку продуктов
        </a>
        """

        return HttpResponse(page('Продукт не найден', content), status=404)

    content = f"""
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{product.name}</h5>
                <p class="card-text">
                    <strong>ID:</strong> {product.id}
                </p>
                <p class="card-text">
                    <strong>Описание:</strong> {product.description}
                </p>
                <p class="card-text">
                    <strong>Страна производства:</strong> {product.country}
                </p>
                <a href="/products/" class="btn btn-outline-secondary">
                    ← к списку продуктов
                </a>
            </div>
        </div>
    """

    return HttpResponse(page(product.name, content))
