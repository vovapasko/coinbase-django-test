from django.views import View
from ..services import BaseApiService, CoingateApiService
import asyncio
from django.http import JsonResponse


class AvailableCurrenciesView(View):
    api_service: BaseApiService = CoingateApiService()

    # TODO: can be cached
    def get(self, request, *args, **kwargs):
        available_currencies = asyncio.run(
            self.api_service.get_supported_currencies()
        )
        return JsonResponse(available_currencies, safe=False)
