from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from storage import load_suppliers
from models.suppliers import Supplier, get_supplier_by_id


def supplier_list(request: HttpRequest) -> HttpResponse:
    suppliers = load_suppliers('data/suppliers.json')

    context: dict[str, list[Supplier]] = {
        "suppliers": suppliers,
    }

    return render(request, "suppliers/supplier_list.html", context)


def supplier_details(request: HttpRequest, supplier_id: int) -> HttpResponse:
    suppliers = load_suppliers('data/suppliers.json')

    supplier = get_supplier_by_id(suppliers, supplier_id)

    context: dict[str, Supplier | None] = {
        "supplier": supplier,
    }

    return render(
        request,
        'suppliers/supplier_detail.html',
        context,
        status=404 if supplier is None else 200,
    )
