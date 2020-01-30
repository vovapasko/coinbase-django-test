from django.shortcuts import render, redirect

# Create your views here.
from .dao import get_currencies, get_all_orders
from .configs import CURRENCIES
from .forms import OrderForm


def index(request):
    now_currency_prices = get_currencies(CURRENCIES)
    print(now_currency_prices)
    all_orders = get_all_orders()
    print(all_orders)
    context = {'currencies': now_currency_prices, 'orders': all_orders}
    return render(request, 'currencyApp/index.html', context=context)


def buy(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print("Here")
        if form.is_valid():
            price_amount = form.cleaned_data['price_amount']
            price_currency = form.cleaned_data['price_currency']
            receive_currency = form.cleaned_data['receive_currency']
            receive_amount = form.cleaned_data['receive_amount']
            print(price_amount, price_currency, receive_currency, receive_amount)
    else:
        form = OrderForm()
    return render(request, 'currencyApp/buy.html', {'form': form})
