from django.urls import reverse_lazy, reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from customer.forms import CustomerForm, UpdateCustomerForm
from customer.models import Customer
from user.models import User


class CreateCustomer(CreateView):
    model = Customer
    template_name = 'customer/create_customer.html'
    form_class = CustomerForm
    success_url = 'customer:create_customer'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        form.creator = self.request.user
        if form.is_valid():
            customer = form
            customer.save()
            return HttpResponseRedirect(reverse('customer:list_customers'))

        return render(request, self.template_name)

    def get_object(self, queryset=None):
        creator = User.objects.get(pk=self.kwargs['pk'])
        return creator

class ListCustomers(ListView):
    model = Customer
    template_name = 'customer/list_customers.html'
    extra_context = {
        'title': 'Список клиентов'
    }


class DetailCustomer(DetailView):
    model = Customer
    template_name = 'customer/detail.html'
    extra_context = {
        'title': 'Информация о клиенте'
    }
    def get_object(self, queryset=None):
        return Customer.objects.get(id=self.kwargs['pk'])

class UpdateCustomer(UpdateView):
    model = Customer
    template_name = 'customer/update_customer.html'
    form_class = UpdateCustomerForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


    def form_valid(self, form):
        super().form_valid(form)
        form.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse_lazy('customer:detail_customer', kwargs={'pk': self.kwargs['pk']})

