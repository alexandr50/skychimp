from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User, UserProfile
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import get_user_model
User = get_user_model()

# username_validator = UnicodeUsernameValidator()

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                                    widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                                 widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
    password1 = forms.CharField(label=_('Password'),
                                    widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})),
                                    help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
                                    help_text=_('Just Enter the same password, for confirmation'))
    username = forms.CharField(
            label=_('Username'),
            max_length=150,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'})
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)




class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'})
    )
    password =forms.CharField(label=_('Password Confirmation'),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),)

    class Meta:
        model = User
        fields = ('username', 'password')



class UserProfileForm(UserChangeForm):

    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        exclude = ('password',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['password'].widget.attrs['hidden'] = True


        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'password')
    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != 'gender':
                field.widget.attrs['class'] = 'form-control py-4'
            else:
                field.widget.attrs['class'] = 'form-control'


