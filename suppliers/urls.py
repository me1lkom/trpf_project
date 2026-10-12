from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('<int:supplier_id>/', views.supplier_details, name='supplier_details')
]
