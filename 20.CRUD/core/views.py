from django.shortcuts import render,redirect
from .models import MarvelModel
from . forms import MarvelForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/')
    else:
        mm= MarvelModel.objects.all()
        mf = MarvelForm()
    return render(request,'core/index.html',{'mf':mf,'mm':mm})



def marvel_delete(request,id):
    mm =MarvelModel.objects.get(pk=id)
    mm.delete()
    return redirect('/')


def marvel_update(request,id):
    if request.method == 'POST':
        mm =MarvelModel.objects.get(pk=id)
        mf = MarvelForm(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()
            return redirect('/')
    else:
        mm =MarvelModel.objects.get(pk=id)
        mf= MarvelForm(instance=mm)
        return render(request,'core/update.html',{'mf':mf})