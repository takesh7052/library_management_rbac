from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
#from home.models import adduser


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/indexuser") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
             # A backend authenticated the credentials
        else:
            return render(request, 'indexuser.html')
             # No backend authenticated the credentials
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")     

def adduser(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        adduser = User(username=username, email=email, password=password)
        adduser.save()
        messages.success(request, 'Your data is submitted!')
    return render(request, 'adduser.html')    

def indexuser(request):
    logout(request)
    return redirect("/indexuser") 