from django.shortcuts import render
from django.views import View
from django.conf import settings

from currencyApp.services import CoingateApiService


class FetchCurrenciesView(View):
    template_name = 'currencyApp/index.html'
    api_service = CoingateApiService()

    def get(self, request, *args, **kwargs):
        now_currency_prices = self.api_service.get_currencies(settings.CURRENCIES)
        all_orders = self.api_service.get_all_orders()
        context = {'currencies': now_currency_prices, 'orders': all_orders}
        return render(request, self.template_name, context=context)
