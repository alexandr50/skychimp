from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from sending.forms import MessageForm, CreateSendingForm
from sending.models import Message, Sending
from user.models import User


class CreateMessage(CreateView):
    model = Message
    template_name = 'sending/create_message.html'
    success_url = 'sending:list_messages'
    form_class = MessageForm

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

class DetailMessage(DetailView):
    model = Message
    template_name = 'sending/detail_message.html'

    def get_object(self, queryset=None):
        message = get_object_or_404(Message, pk=self.kwargs['pk'])
        return message #Message.objects.get(pk=self.kwargs['pk'])

class UpdateMessage(UpdateView):
    model = Message
    template_name = 'sending/update_message.html'
    form_class = MessageForm

    def form_valid(self, form):
        super().form_valid(form)
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('sending:detail_message', kwargs={'pk': self.kwargs['pk']})

class DeleteMessage(DeleteView):
    model = Message
    success_url = reverse_lazy('sending:list_messages')


class ListSending(ListView):
    model = Sending
    template_name = 'sending/list_sending.html'

    def get_queryset(self):
        return Sending.objects.all()

class CreateSending(CreateView):
    model = Sending
    template_name = 'sending/create_sending.html'
    form_class = CreateSendingForm
    success_url = 'sending:list_sending'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)  # Подготовиться обьект с данными из формы
            self.object.user_create = self.request.user  # В поле user_create запишится пользователь который делает запрос
            self.object.save()
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = CreateSendingForm(data=request.POST)
    #     if form.is_valid():
    #         sending = form.save(commit=False)
    #         sending.user = self.request.user
    #         sending.save()
    #         return HttpResponseRedirect(reverse('sending:list_sending'))
    #
    #     return render(request, self.template_name)

    def get_object(self, queryset=None):
        user = User.objects.get(pk=self.kwargs['pk'])
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request.user})
        return kwargs



