import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'demo/index.html')


def deal_get(request):
    if request.method == 'GET':
        value = request.GET['key1']
        context = {'key': value, 'method': 'get'}
        return HttpResponse(json.dumps(context))


def deal_post(request):
    if request.method == 'POST':
        value = request.POST['key1']
        context = {'key': value, 'method': 'post'}
        return HttpResponse(json.dumps(context))
