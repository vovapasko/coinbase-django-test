from django.shortcuts import render, redirect

# Create your views here.
from .dao import get_currencies, get_all_orders, make_order
from .configs import CURRENCIES
from .forms import OrderForm
import uuid


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
            print(price_amount, price_currency, receive_currency)
            order_id = uuid.uuid4()
            response = make_order(order_id, price_amount, price_currency, receive_currency)
            print(response.status_code)
            if response.status_code == 200:
                redirect('index')
            else:
                return render(request, 'currencyApp/buy.html', {'form': form, 'error_message': str(response.json()['errors'])})
    else:
        form = OrderForm()
    return render(request, 'currencyApp/buy.html', {'form': form})
