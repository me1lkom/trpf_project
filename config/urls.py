from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('products/', include('products.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('offers/', include('offers.urls'))
]

handler404 = 'homepage.views.page_not_found'
