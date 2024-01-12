from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
   return render(request,'index.html')
def signUp(request):
    if request.method=="POST":
     uname=request.POST.get('username')
     email=request.POST.get('email')
     pass1=request.POST.get('password1')
     pass2=request.POST.get('password2')
     if pass1!=pass2:
        return HttpResponse("Your passwords do not match")
     my_user=User.objects.create_user(uname,email,pass1)
     my_user.save()
     return redirect('login')
    return render(request,'home.html')

def log_in(request):
    if request.method=="POST":
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username, password=password)
       if user is not None:
          login(request,user)
          return redirect('index')
       else:
          return HttpResponse("User doesnot match")
       
    return render(request,'login.html')