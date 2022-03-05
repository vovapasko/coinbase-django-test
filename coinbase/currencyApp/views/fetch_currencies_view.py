from django.shortcuts import render
from django.views import View
from django.conf import settings

from currencyApp.dao import get_all_orders, get_currencies


class FetchCurrenciesView(View):
    template_name = 'currencyApp/index.html'

    def get(self, request, *args, **kwargs):
        now_currency_prices = get_currencies(settings.CURRENCIES)
        all_orders = get_all_orders()
        context = {'currencies': now_currency_prices, 'orders': all_orders}
        return render(request, self.template_name, context=context)
