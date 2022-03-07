from django.shortcuts import render
from django.views import View
from django.conf import settings

from ..services import BaseApiService, CoingateApiService
import asyncio


class FetchCurrenciesView(View):
    template_name = 'currencyApp/index.html'
    api_service: BaseApiService = CoingateApiService()

    def get(self, request, *args, **kwargs):
        now_currency_prices = asyncio.run(
            self.api_service.get_currencies())
        all_orders = asyncio.run(self.api_service.get_all_orders())
        context = {'currencies': now_currency_prices, 'orders': all_orders}
        return render(request, self.template_name, context=context)
