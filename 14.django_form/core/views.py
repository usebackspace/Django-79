from django.shortcuts import render,redirect
from .forms import MarvelForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})


def form_post(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            f_name = mf.cleaned_data['first_name']
            l_name = mf.cleaned_data['last_name']
            h_name = mf.cleaned_data['heroic_name']
            print(f_name)
            print(l_name)
            print(h_name)
            # mf = MarvelForm()
            # return HttpResponse('Successfully submitted')           
            # return render(request,'core/success.html')
            return redirect('/success/')
    else:
        mf= MarvelForm()
        print('===')
    return render(request,'core/form_post.html',{'mf':mf})

def success(request):
    return render(request,'core/success.html')