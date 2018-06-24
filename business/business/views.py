from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    #return HttpResponse('home')
    return render(request, 'index.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')

def products(request):
    #return HttpResponse('products')
    return render(request, 'products.html')

def store(request):
    #return HttpResponse('store')
    return render(request, 'store.html')