from django.shortcuts import render
from . models import Marvel
# Create your views here.

def index(request):
    mf = Marvel.objects.all()
    return render(request,'core/index.html',{'mf':mf})