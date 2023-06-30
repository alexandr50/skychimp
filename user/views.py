from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages

from skychimp import settings
from user.forms import UserRegisterForm, UserLoginForm, UserProfileForm, UserProfileEditForm
from user.mixin import BaseClassContextMixin, UserDispatchMixin
from user.models import User
from user.utils import generate_code


class RegisterUser(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    # success_url = reverse_lazy('user:login')
    extra_context = {
        'title': 'Регистрация'
    }

    def get_success_url(self):
        return reverse('user:confirm_code', kwargs={'email': self.object.email})

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            code = generate_code()
            new_user.verify_code = code
            new_user.save()
            send_mail(
                subject='Вы зарегистрировались',
                message=code,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )

        return super().form_valid(form)

def confirm_code(request, email):
    if request.method == 'POST':
        verify_code = request.POST.get('verify_code')
        user = User.objects.get(email=email)
        if user.verify_code == verify_code:
            user.is_active = True
            user.save()
            return redirect(reverse('user:login'))
        else:
            raise ValidationError(f'You have used the wrong code!')
    else:
        context = {'title': 'Подтверждение почты'}

    return render(request, 'user/confirm_code.html', context)



class LoginUser(LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('user:profile')
    extra_context = {
        'title': 'Авторизация'
    }


class ProfileUser(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('user:profile')
    extra_context = {
        'title': 'Профиль'
    }

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(data=request.POST, instance=request.user)
        # profile_form = UserProfileEditForm(data=request.POST, instance=request.user.userprofile)
        if form.is_valid():
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
    extra_context = {
        'title': 'Выход'
    }
