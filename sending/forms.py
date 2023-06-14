from django import forms

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
    # customer = forms.MultipleChoiceField(
    #     choices=[(customer, customer) for customer in
    #              Customer.objects.all()])
    #
    # message = forms.ChoiceField(
    #     choices=[(message, message) for message in Message.objects.all()],
    #     widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Письмо'}))
    #
    # interval = forms.ChoiceField(choices=Sending.INTERVAL,
    #                              widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Интервал'}))
    # status_sending = forms.ChoiceField(choices=Sending.STATUS,
    #                                    widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Стaтус'}))

    class Meta:
        model = Sending
        fields = ('interval', 'status_sending', 'customer', 'message')

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)

        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(
            customer=self.request)
        self.fields['message'].queryset = Message.objects.filter(
            user=self.request)
