from django.urls import path
from .views import MainView, BuyCurrencyView, AvailableCurrenciesView

app_name = 'currencyApp'
urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('buy/', BuyCurrencyView.as_view(), name='buy_currency_view'),
    path('get-all/', AvailableCurrenciesView.as_view(), name='available_currencies')
]
