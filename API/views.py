from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from rest_framework.views import APIView

class CurrencyExchangeRateApi(APIView):

	def post(self, request, format=None):
		print(request.data)
		currency_from = request.data.get('currency_from')
		currency_to = request.data.get('currency_to')
		currency_joined = currency_from + '_' + currency_to
		url = 'https://free.currencyconverterapi.com/api/v5/convert?q=' + currency_joined + '&compact=ultra'
		r = requests.get(url)
		request_data = json.loads(r.text)
		response = {
			"messages": [
				{"text": "Currency rate from" + currency_from + " to " + currency_to + " is:"},
		   		{"text": str(request_data[currency_joined])}
		 	]
		}
		return JsonResponse(response)

	def get(self, request, format=None):
		return HttpResponse("Get request; Use Post request")

class CurrencyConvertApi(APIView):

	def post(self, request, format=None):
		currency_from = request.data.get('currency_from')
		currency_to = request.data.get('currency_to')
		amount = request.data.get('amount')
		currency_joined = currency_from + '_' + currency_to
		url = 'https://free.currencyconverterapi.com/api/v5/convert?q=' + currency_joined + '&compact=ultra'
		r = requests.get(url)
		request_data = json.loads(r.text)
		converted_amount = float(amount) * request_data[currency_joined]
		response = {
			"messages": [
				{"text": "Your " + str(amount) + ' ' + currency_from + " convert to " + str(converted_amount) + ' ' + currency_to }
		 	]
		}
		return JsonResponse(response)

	def get(self, request, format=None):
		return HttpResponse("Get request; Use Post request")
