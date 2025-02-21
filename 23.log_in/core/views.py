from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import Register
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = Register(request.POST)
            if mf.is_valid():
                mf.save()
                messages.success(request,'Registration Successfull')
                return redirect('/')
        else:
            mf=Register()
        return render(request,'core/signup.html',{'mf':mf})
    else:
        return redirect('/profile/')

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = AuthenticationForm(request,data=request.POST)
            if mf.is_valid():
                un = mf.cleaned_data['username']
                up = mf.cleaned_data['password']
                user = authenticate(username=un,password=up)
                if user is not None:
                    login(request,user)
                    return redirect('/profile/')
        else:
            mf=AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('/profile/')
    

def profile(request):
    if request.user.is_authenticated:
        return render(request,'core/profile.html')
    else:
        return redirect('/login/')

def user_logout(request):
    logout(request)
    return redirect('/login/')