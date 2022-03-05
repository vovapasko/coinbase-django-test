from django.urls import path
from .views import FetchCurrenciesView, BuyCurrencyView

app_name = 'currencyApp'
urlpatterns = [
    path('', FetchCurrenciesView.as_view(), name='fetch_currencies_view'),
    path('buy/', BuyCurrencyView.as_view(), name='buy_currency_view'),
]
