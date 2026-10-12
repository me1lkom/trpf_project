from django.http import HttpResponse

from homepage.views import page
from storage import load_suppliers
from models.suppliers import get_supplier_by_id


def supplier_list(request):
    items = ''

    for supplier in load_suppliers('data/suppliers.json'):
        items += (
            '<li class="list-group-item">'
            f'<a href="/suppliers/{supplier.id}/">'
            f'{supplier.name} — {supplier.phone}'
            '</a>'
            '</li>'
        )

    content = f"""
        <h1>Поставщики</h1>
        <ul class="list-group">{items}</ul>
    """

    return HttpResponse(page('Список поставщиков', content))


def supplier_details(request, supplier_id):
    suppliers = load_suppliers('data/suppliers.json')

    supplier = get_supplier_by_id(suppliers, supplier_id)

    if supplier is None:
        content = """
        <h1 class="text-danger">Поставщик не найден</h1>
        <a href="/suppliers/" class="btn btn-outline-secondary">
            ← к списку поставщиков
        </a>
        """

        return HttpResponse(page('Поставщик не найден', content), status=404)

    content = f"""
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{supplier.name}</h5>
                <p class="card-text">
                    <strong>ID:</strong> {supplier.id}
                </p>
                <p class="card-text">
                    <strong>ИНН:</strong> {supplier.inn}
                </p>
                <p class="card-text">
                    <strong>Телефон:</strong> {supplier.phone}
                </p>
                <p class="card-text">
                    <strong>Email:</strong> {supplier.email}
                </p>
                <a href="/suppliers/" class="btn btn-outline-secondary">
                    ← к списку поставщиков
                </a>
            </div>
        </div>
    """

    return HttpResponse(page(supplier.name, content))
