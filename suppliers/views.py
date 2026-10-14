from django.shortcuts import render

from storage import load_suppliers
from models.suppliers import get_supplier_by_id


def supplier_list(request):
    suppliers = load_suppliers('data/suppliers.json')

    context = {
        "suppliers": suppliers,
    }

    return render(request, "suppliers/supplier_list.html", context)


def supplier_details(request, supplier_id):
    suppliers = load_suppliers('data/suppliers.json')

    supplier = get_supplier_by_id(suppliers, supplier_id)

    context = {
        "supplier": supplier,
    }

    return render(
        request,
        'suppliers/supplier_detail.html',
        context,
        status=404 if supplier is None else 200,
    )
