from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
    path('buy/<int:id>/', views.initiate_payment, name='initiate_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),


]
