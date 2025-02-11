from django.shortcuts import render
from .forms import MarvelForm
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
            mf = MarvelForm()
    else:
        mf= MarvelForm()
        print('===')
    return render(request,'core/form_post.html',{'mf':mf})