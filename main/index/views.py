from django.shortcuts import render
from django.http import HttpResponse

def teste(request):
    context = {"testador":"madruguinha"}
    return render(request, 'index/index.html', context)