# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def staffing(request):
    return render(request,'staffing.html')

def pharmastaffing(request):
    return render(request,'pharmastaffing.html')

def md(request):
    return render(request,'mobile-apps.html')

def web(request):
    return render(request,'web-apps.html')

def digital(request):
    return render(request,'dm.html')  

def arch(request):
    return render(request,'architectures.html') 

def careers(request):
    return render(request,'careers.html') 
    
def contacts(request):
    return render(request,'contact.html')