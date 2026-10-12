from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_details, name='product_details')
]
