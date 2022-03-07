from django import forms

from currencyApp.models import CoingateOrder


class CoingateOrderForm(forms.ModelForm):
    class Meta:
        model = CoingateOrder
        fields = ['price_amount', 'price_currency', 'receive_currency']

    price_amount = forms.FloatField(label='Price amount', required=True)
    price_currency = forms.ChoiceField(choices=[("BTC", "BTC"), ("USD", "USD"), ("EUR", "EUR")], required=True)
    receive_currency = forms.ChoiceField(choices=[("BTC", "BTC"), ("USD", "USD"), ("EUR", "EUR")], required=True)
