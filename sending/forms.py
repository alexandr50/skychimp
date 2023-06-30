from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import DateTimeInput

from customer.models import Customer
from sending.models import Message, Sending


class MessageForm(forms.ModelForm):
    theme = forms.CharField(max_length=50, min_length=4, required=True, help_text='Required: First Name',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Тема'}))
    content = forms.CharField(max_length=200, min_length=4, required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Контент'}))

    class Meta:
        model = Message
        fields = ('theme', 'content')


class CreateSendingForm(forms.ModelForm):
    # customer = forms.ModelMultipleChoiceField(
    #     queryset=Customer.objects.all(),
    #     empty_label='all',
    #     widget=forms.Select(attrs={'class': 'radioselect'}), required=False, label='Клиент')

    #
    # message = forms.ChoiceField(
    #     choices=[(message, message.theme) for message in Message.objects.all()],
    #     widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Письмо'}))
    #
    # interval = forms.ChoiceField(choices=Sending.INTERVAL,
    #                              widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Интервал'}))
    # status_sending = forms.ChoiceField(choices=Sending.STATUS,
    #                                    widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Стaтус'}))

    # time_sending = forms.DateTimeField(
    #     required=False,
    #     widget=DateTimeInput(attrs={'type': 'datetime-local'}),
    #     initial=datetime.now(),
    #     localize=True
    # )

    start_sending = forms.DateTimeField(
        required=False,
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=datetime.now(),
        localize=True
    )
    end_sending = forms.DateTimeField(
        required=False,
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=datetime.now(),
        localize=True
    )

    class Meta:
        model = Sending
        exclude = ('user',)


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()
        self.fields['message'].queryset = Message.objects.filter(
            user=self.request)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UpdateSendingForm(forms.ModelForm):
    
    start_sending = forms.DateTimeField(
        required=False,
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=datetime.now(),
        localize=True
    )
    end_sending = forms.DateTimeField(
        required=False,
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=datetime.now(),
        localize=True
    )

    class Meta:
        model = Sending
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UpdateSendingForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = True

        # self.fields['created_at'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


