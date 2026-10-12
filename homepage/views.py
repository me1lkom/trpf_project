from django.http import HttpResponse


def page(title: str, content: str) -> str:
    bootstrap = (
        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3'
        '/dist/css/bootstrap.min.css'
    )

    return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width,
                initial-scale=1">
            <title>{title}</title>
            <link rel="stylesheet" href="{bootstrap}">
        </head>
        <body>
            <nav class="nav">
                <a class="nav-link" href="/">Главная</a>
                <a class="nav-link" href="/products/">Товары</a>
                <a class="nav-link" href="/suppliers/">Поставщики</a>
                <a class="nav-link" href="/offers/">Предложения</a>
            </nav>
            <main class="container mt-4">
                {content}
            </main>
        </body>
        </html>
    """


def index(request):
    content = """
        <h1 class="display-4">Сервис сравнения предложений</h1>
        <p class="lead">Выбор выгодных предложений поставщиков.</p>
        <a href="/products/" class="btn btn-primary">Товары</a>
        <a href="/suppliers/" class="btn btn-secondary">Поставщики</a>
        <a href="/offers/" class="btn btn-secondary">Предложения</a>
    """

    return HttpResponse(page('Главная', content))


def page_not_found(request, exception):
    content = """
        <h1 class="text-danger">404 – страница не найдена</h1>
        <p>Проверьте адрес или вернитесь на главную.</p>
        <a href="/" class="btn btn-primary">На главную</a>
    """

    return HttpResponse(page('404 – страница не найдена', content), status=404)
