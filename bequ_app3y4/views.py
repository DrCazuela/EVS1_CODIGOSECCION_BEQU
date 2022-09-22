from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista3(request):
    return HttpResponse('<h1>Ahora si, contra un jefe mas serio</h1><br><img src="https://i.kym-cdn.com/photos/images/newsfeed/001/115/364/4bc.jpg_large">')

def vista4(request):
    return HttpResponse('<h1>Ahora contra el jefe final</h1><br><img src="https://img-9gag-fun.9cache.com/photo/ayxNz1q_700bwp.webp">')