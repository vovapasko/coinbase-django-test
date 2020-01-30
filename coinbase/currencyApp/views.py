from django.shortcuts import render

# Create your views here.
from .dao import get_currencies
from .configs import CURRENCIES


def index(request):
    now_currency_prices = get_currencies(CURRENCIES)
    print(now_currency_prices)
    context = {'currencies': now_currency_prices}
    return render(request, 'currencyApp/index.html', context=context)
