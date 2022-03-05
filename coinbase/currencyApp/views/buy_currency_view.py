import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from currencyApp.dao import make_order
from currencyApp.forms import OrderForm


class BuyCurrencyView(View):
    template_name = 'currencyApp/buy.html'
    form = OrderForm()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        self.form = OrderForm(request.POST)
        print("Here")
        if self.form.is_valid():
            price_amount = self.form.cleaned_data['price_amount']
            price_currency = self.form.cleaned_data['price_currency']
            receive_currency = self.form.cleaned_data['receive_currency']
            print(price_amount, price_currency, receive_currency)
            order_id = uuid.uuid4()
            response = make_order(order_id, price_amount, price_currency, receive_currency)
            print(response.status_code)
            if response.status_code == 200:
                return HttpResponseRedirect('/money')
            else:
                return render(request, self.template_name,
                              {'form': self.form, 'error_message': str(response.json()['errors'])})
