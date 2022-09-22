from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1 (request):
    return HttpResponse('<h1> Estamos iniciando </h1>')

def vista2 (request):
    return HttpResponse('<h1>Mientras tanto espere con un perro</h1><br><img src="https://images3.memedroid.com/images/UPLOADED501/60d4a37af0241.jpeg">')