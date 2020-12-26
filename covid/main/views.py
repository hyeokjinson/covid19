from django.shortcuts import render
import requests
import json
def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country": "uk"}

    headers = {
        'x-rapidapi-key': "6db88208bemsh9c104ec023d5c4ap1f1d23jsn69fc2b19b2e9",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data=response['response']
    d=data[0]

    print(d)

    context={
        'all':d['cases']['total'],
        'recovered':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical']
    }
    return render(request,'index.html',context)


