from django.shortcuts import redirect, render
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
# Create your views here.

def product(request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'product.html',{'product': product} )

def home(request):
        products = Product.objects.all()
        return render(request, 'home.html',{'products': products})
        
def about(request):
        return render(request,'about.html',{})

def login_user(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username = username, password = password)
                if user is not None:
                        login(request,user)
                        messages.success(request,"You have been logged in!!!")
                        return redirect('home')
                else:
                        messages.success(request,"There is an error, pls login again!!!")
                        return redirect('login')




        else:
                 return render(request,'login.html',{})

def logout_user(request):
        logout(request)
        messages.success(request,("You have been logged out ..."))
        return redirect('home')

def register(request):
        form = SignUpForm()
        if request.method == "POST":
                form = SignUpForm(request.POST)
                if form.is_valid:
                        form.save()
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password1']

                        user = authenticate(username = username, password = password)
                        login(request,user)
                        messages.success(request, "You have Register success")
                        return redirect ('home')
                else:
                        messages.success(request, "Oop, you have problem in Register. Pls register again!!!")
                        return redirect ('register')
        else:
                return render(request,'register.html',{'form' : form})
        


def category(request,foo):
        foo = foo.replace('-' , ' ')
        try:
                category = Category.objects.get(name=foo)
                products = Product.objects.filter(category = category)
                return render(request,'category.html',{'category': category, 'products' : products})

        
        except:
                messages.success(request,"That category doesn't exist!!!")
                return redirect('home')



