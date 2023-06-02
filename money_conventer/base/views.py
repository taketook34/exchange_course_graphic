from django.shortcuts import render
from django.http import HttpResponse
import requests

#menu = ['Головна', 'Регістрація', 'Створити курс']

def home(request):
    response = requests.get(url='https://v6.exchangerate-api.com/v6/ef7afc5c6a6b569279edff98/latest/USD').json()
    currency = response.get('conversion_rates')
    print(currency)

    if request.method == 'GET':
        context = {
            'currency': currency,
            'title':'Головна',
        }
        return render(request, 'base/index.html', context=context)

    if request.method == "POST":
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        print(to_curr)
        print(from_curr)
        result = (currency[to_curr] / currency[from_curr]) * float(from_amount)
        converted_amount = round(result, 2)

        context = {
            'currency': currency,
            'title': 'Головна',
            'converted_amount': converted_amount,
        }
        return render(request, 'base/index.html', context=context)


# Create your views here.
