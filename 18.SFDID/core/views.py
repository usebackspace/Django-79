from django.shortcuts import render
from . forms import MarvelForm
from . models import MarvelModel
# Create your views here.

def index(request):
    if request.method =='POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            f_name = mf.cleaned_data['name']
            h_name = mf.cleaned_data['heroic_name']
            print(f_name)
            print(h_name)
            MarvelModel(name=f_name,heroic_name=h_name).save()
            mf=MarvelForm()
    else:
        mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})