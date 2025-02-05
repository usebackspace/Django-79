from django.shortcuts import render

# Create your views here.
def spiderman(request):
    # context={'willian':'Eleo'}
    return render(request,'marvel/spiderman.html',{'willian':'thanos'})

def ironman(request):
    # for loop
    context ={'willian':['Thanos','Zola','Hella','Loki','Venom','Goblin']}
    return render(request,'marvel/ironman.html',context)