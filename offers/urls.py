from django.urls import path
from . import views

urlpatterns = [
    path('', views.offer_list, name='offer_list'),
    path('<int:offer_id>/', views.offer_details, name='offer_details')
]
