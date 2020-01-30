from django import forms


class OrderForm(forms.Form):
    price_amount = forms.FloatField(label='Price amount', required=True)
    price_currency = forms.ChoiceField(choices=[("BTC", "BTC"), ("USD", "USD"), ("EUR", "EUR")], required=True)
    receive_currency = forms.ChoiceField(choices=[("BTC", "BTC"), ("USD", "USD"), ("EUR", "EUR")], required=True)
