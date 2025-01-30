from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1> This is a Home of our heros </h1>')

def about(request):
    return HttpResponse('Hello Heros What about you')


def contact(request):
    return HttpResponse('Hello Heros contact in emergency')