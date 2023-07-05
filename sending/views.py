from datetime import datetime, date, time

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.utils import timezone

from customer.models import Customer
from sending.cron import sending_mail
from sending.forms import MessageForm, CreateSendingForm, UpdateSendingForm
from sending.models import Message, Sending
from skychimp import settings
from user.models import User


class CreateMessage(CreateView):
    model = Message
    template_name = 'sending/create_message.html'
    success_url = 'sending:list_messages'
    form_class = MessageForm
    extra_context = {
        'title': 'Создание письма'
    }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        form.user = self.request.user
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return HttpResponseRedirect(reverse(self.success_url))
        return render(request, self.template_name)


class ListMessages(ListView):
    model = Message
    template_name = 'sending/list_messages.html'
    extra_context = {
        'title': 'Список писем'
    }


class DetailMessage(DetailView):
    model = Message
    template_name = 'sending/detail_message.html'
    extra_context = {
        'title': 'Информация о письме'
    }

    def get_object(self, queryset=None):
        message = get_object_or_404(Message, pk=self.kwargs['pk'])
        return message  # Message.objects.get(pk=self.kwargs['pk'])


class UpdateMessage(PermissionRequiredMixin, UpdateView):
    permission_required = 'sending.change_message'
    model = Message
    template_name = 'sending/update_message.html'
    form_class = MessageForm
    extra_context = {
        'title': 'Обновление информации о письме'
    }

    def form_valid(self, form):
        super().form_valid(form)
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('sending:detail_message', kwargs={'pk': self.kwargs['pk']})


class DeleteMessage(DeleteView):
    model = Message
    success_url = reverse_lazy('sending:list_messages')
    extra_context = {
        'title': 'Информация о письме'
    }


class ListSending(ListView):
    model = Sending
    template_name = 'sending/list_sending.html'
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        global result
        query_sending = Sending.objects.exclude(status_sending='завершена')
        #     .filter(start_sending=timezone.now()) \
        #     .filter(next_run=timezone.now())
        # print(1)
        # with open('file.txt', 'w') as file:
        #     file.write(f'mjgndjkd')
        #

        # for sending in query_sending:
        #     print(sending.start_sending_date)
        #     print(sending.start_sending_time)
        #     print(type(sending.start_sending_time))
        #     print(sending.next_run)
        #     print(date.today())
        #     print(datetime.now().time().strftime("%H:%M:%S"))
        #     my_time = time(*list(map(int, datetime.now().time().strftime("%H:%M:%S").split(':'))))
        #     print(type(my_time))
        #     print('--------------')
        #     print(sending.start_sending_date == date.today())
        #     print(sending.start_sending_time == my_time)
        s = Customer.objects.get(first_name='liza')
        try:
            result = send_mail(
                subject='Sending',
                message='Вам письмо',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[s.email],
                # fail_silently=False
            )
            print(result)
            print(s.email)
        except Exception as err:

            print(err)

        return Sending.objects.all()


class CreateSending(CreateView):
    model = Sending
    template_name = 'sending/create_sending.html'
    form_class = CreateSendingForm
    success_url = reverse_lazy('sending:list_sending')
    extra_context = {
        'title': 'Создание рассылки'
    }

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request.user})
        return kwargs


class UpdateSendingView(PermissionRequiredMixin, UpdateView):
    permission_required = 'sending.change_sending'
    model = Sending
    template_name = 'sending/update_sending.html'
    form_class = UpdateSendingForm
    extra_context = {
        'title': 'Обновление информации о рассылке'
    }

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = UpdateSendingForm(data=self.request.POST, instance=self.request.user)
            if form.is_valid():
                form.instance = self.object
                form.updated_at = timezone.now()
                form.save()
        else:
            form = UpdateSendingForm(instance=self.request.user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sending:detail_sending', kwargs={'pk': self.kwargs['pk']})


class DetailSending(PermissionRequiredMixin, DetailView):
    permission_required = 'sendind.view_sending'
    model = Sending
    template_name = 'sending/detail_sending.html'
    extra_context = {
        'title': 'Информация о рассылке'
    }

    def get_object(self, queryset=None):
        sending = Sending.objects.get(pk=self.kwargs['pk'])
        return sending


class DeleteSendingView(DeleteView):
    model = Sending
    extra_context = {
        'title': 'Удаление рассылки'
    }

    def get_success_url(self):
        return reverse_lazy('sending:list_sending')
