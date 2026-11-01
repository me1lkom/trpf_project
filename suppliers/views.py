from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from suppliers.models import Supplier, SupplierMember
from offers.models import Offer


def supplier_list(request: HttpRequest) -> HttpResponse:
    searching_supplier = request.GET.get('search', default='').strip()

    suppliers: QuerySet[Supplier]

    if searching_supplier == '':
        suppliers = (
            Supplier
            .objects
            .all()
        )
    else:
        suppliers = (
            Supplier
            .objects
            .filter(name__icontains=searching_supplier)
        )

    context: dict[str, QuerySet[Supplier] | str] = {
        'suppliers': suppliers,
        'searching_supplier': searching_supplier
    }

    return render(request, "suppliers/supplier_list.html", context)


def supplier_details(request: HttpRequest, supplier_id: int) -> HttpResponse:
    supplier: Supplier = get_object_or_404(
        Supplier.objects.prefetch_related(
            'offers__product',
            'members__user',
        ),
        pk=supplier_id
    )

    offers: QuerySet[Offer] = supplier.offers.all()
    members: QuerySet[SupplierMember] = supplier.members.all()

    context = {
        'supplier': supplier,
        'offers': offers,
        'members': members
    }

    return render(
        request,
        'suppliers/supplier_detail.html',
        context,
    )
