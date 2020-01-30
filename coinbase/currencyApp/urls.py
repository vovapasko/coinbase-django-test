from django.urls import path

from . import views

app_name = 'currencyApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
]