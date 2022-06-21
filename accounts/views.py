from django.shortcuts import render,redirect
from .form import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('user')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
    return render(request,'index.html')

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'register.html',context)

@login_required(login_url='home')
def profile(request):
    return render(request,'profile.html')

def logoutpage(request):
    logout(request)
    return redirect('home')
