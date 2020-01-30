from django.shortcuts import render

# Create your views here.
from .dao import get_currencies, get_all_orders
from .configs import CURRENCIES


def index(request):
    now_currency_prices = get_currencies(CURRENCIES)
    print(now_currency_prices)
    all_orders = get_all_orders()
    print(all_orders)
    context = {'currencies': now_currency_prices, 'orders': all_orders}
    return render(request, 'currencyApp/index.html', context=context)


def buy(request):
    return render(request, 'currencyApp/buy.html')
