from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Register
# Create your views here.

# def signup(request):
#     if request.method == 'POST':
#         mf = UserCreationForm(request.POST)
#         if mf.is_valid():
#             mf.save()
#             messages.success(request,'Registration Successfull')
#             return redirect('/')
#     else:
#         mf=UserCreationForm()
#     return render(request,'core/signup.html',{'mf':mf})

def signup(request):
    if request.method == 'POST':
        mf = Register(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'Registration Successfull')
            return redirect('/')
    else:
        mf=Register()
    return render(request,'core/signup.html',{'mf':mf})