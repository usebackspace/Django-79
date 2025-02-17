from django.shortcuts import render
from . models import MarvelModel
from . forms import MarvelForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
            mf=MarvelForm()
    else:
       mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})