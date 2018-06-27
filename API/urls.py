from django.urls import path

from . import views

urlpatterns = [
    path('currency_exchange_rate', views.CurrencyExchangeRateApi.as_view()),
    path('convert_currency', views.CurrencyConvertApi.as_view()),
]
