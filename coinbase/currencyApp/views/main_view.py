from django.shortcuts import render
from django.views import View
from django.conf import settings

from ..services import BaseApiService, CoingateApiService
import asyncio


class MainView(View):
    template_name = 'currencyApp/index.html'
    api_service: BaseApiService = CoingateApiService()

    def get(self, request, *args, **kwargs):
        now_currency_prices = asyncio.run(
            self.fetch_main_currencies()
        )
        all_orders = asyncio.run(self.api_service.get_all_orders())
        context = {'currencies': now_currency_prices, 'orders': all_orders}
        return render(request, self.template_name, context=context)

    async def fetch_main_currencies(self) -> dict:
        values = {}
        for currency in settings.CURRENCIES:
            value = await self.api_service.get_exchange_rate(_from=currency.get('_from'), _to=currency.get('_to'))
            values[currency.get('_to')] = value
        return values
