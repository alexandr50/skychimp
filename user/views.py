from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages
from user.forms import UserRegisterForm, UserLoginForm, UserProfileForm, UserProfileEditForm
from user.mixin import BaseClassContextMixin, UserDispatchMixin
from user.models import User


class RegisterUser(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form
            user.save()
            return HttpResponseRedirect(reverse('user:login'))
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        context = {'form': form}
        return render(request, self.template_name, context)



class LoginUser(LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('user:profile')


class ProfileUser(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('user:profile')

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(data=request.POST, instance=request.user)
        profile_form = UserProfileEditForm(data=request.POST, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
        return redirect(self.success_url)


    def get_object(self, queryset=None):

        return User.objects.get(id=self.request.user.pk)


    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.error(self.request, 'Данные изменены')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class LogoutUser(LogoutView):
    template_name = 'user/login.html'
