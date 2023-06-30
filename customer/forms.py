from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError

from customer.models import Customer
from user.models import User


class CustomerForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: First Name',
    #                              widget=forms.TextInput(
    #                                  attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    # last_name = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: Last Name',
    #                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})))
    # email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
    #                          widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
    # comment = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: Last Name',
    #                            widget=(forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Коментарий'})))

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        # self.fields['creator'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def clean_email(self):
        new_email = self.cleaned_data['email']
        if Customer.objects.filter(email=new_email).exists():
            raise ValidationError('Почта уже занята')
        return new_email


class UpdateCustomerForm(UserChangeForm):
    # first_name = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: First Name',
    #                              widget=forms.TextInput(
    #                                  attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    # last_name = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: Last Name',
    #                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})))
    # email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
    #                          widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
    # comment = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: Last Name',
    #                           widget=(forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Коментарий'})))

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super(UpdateCustomerForm, self).__init__(*args, **kwargs)
        # self.fields['creator'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'



