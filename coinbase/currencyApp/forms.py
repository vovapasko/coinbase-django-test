from django import forms

from currencyApp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['order_id']

    price_amount = forms.FloatField(label='Price amount', required=True)
    price_currency = forms.ChoiceField(choices=[("BTC", "BTC"), ("USD", "USD"), ("EUR", "EUR")], required=True)
    receive_currency = forms.ChoiceField(choices=[("BTC", "BTC"), ("USD", "USD"), ("EUR", "EUR")], required=True)
