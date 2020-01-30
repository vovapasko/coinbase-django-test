from django import forms


class OrderForm(forms.Form):
    price_amount = forms.FloatField(label='Price amount')
    price_currency = forms.ChoiceField(choices=[("btc", "BTC"), ("usd", "USD"), ("eur", "EUR")])
    receive_currency = forms.ChoiceField(choices=[("btc", "BTC"), ("usd", "USD"), ("eur", "EUR")])
    receive_amount = forms.FloatField(label="Receive amount")
