from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'homepage/index.html')


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(
        request,
        '404.html',
        status=404,
    )
