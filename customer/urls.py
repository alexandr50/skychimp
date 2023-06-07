from django.urls import path

from customer.views import CreateCustomer, ListCustomers, DetailCustomer, UpdateCustomer

app_name = 'customer'

urlpatterns = [
    path('create_customer', CreateCustomer.as_view(), name='create_customer'),
    path('list_customers', ListCustomers.as_view(), name='list_customers'),
    path('detail_customer/<int:pk>/', DetailCustomer.as_view(), name='detail_customer'),
    path('update_customer/<int:pk>/', UpdateCustomer.as_view(), name='update_customer'),

]
