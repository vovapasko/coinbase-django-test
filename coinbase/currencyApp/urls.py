from django.urls import path

from coinbase.currencyApp import views

urlpatterns = [
    path('', views.index, name='index')

]