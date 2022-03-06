import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from currencyApp.forms import CoingateOrderForm

from currencyApp.services import CoingateApiService



class BuyCurrencyView(View):
    template_name = 'currencyApp/buy.html'
    form = CoingateOrderForm()
    api_service = CoingateApiService()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        self.form = CoingateOrderForm(request.POST)
        if self.form.is_valid():
            order = self.form.save()
            response = self.api_service.make_order(order)
            if response.status_code == 200:
                # TODO: provide saving invoice in db
                return HttpResponseRedirect('/money')
            return render(request, self.template_name,
                          {'form': self.form, 'error_message': str(response.json()['errors'])})
        return render(request, self.template_name, {'form': self.form})