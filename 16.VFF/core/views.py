from django.shortcuts import render,redirect
from .forms import MarvelForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            
            # mf = MarvelForm()
            # return HttpResponse('Successfully submitted')           
            # return render(request,'core/success.html')
            return redirect('/success/')
    else:
        mf= MarvelForm()
        print('===')
    return render(request,'core/index.html',{'mf':mf})

def success(request):
    return render(request,'core/success.html')