from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def about(request,id):
    print('===',id)
    return render(request,'core/about.html')

def aboutshoes(request,str,id):
    print('===',str)
    print('===',id)
    return render(request,'core/about.html')