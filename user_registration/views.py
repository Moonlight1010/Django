from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def register(request):
    form = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have sucessfully created an account')
            return redirect('login-page')
        else:
            form = UserRegistrationForm()
    else:
        form = UserRegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'user_registration/register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            if user.is_active:
                auth.login(request,user) 
                return redirect('blog-name')
            else:
                messages.error(request, 'Account is not active')
                return render(request, 'user_registration/login.html')

        elif user is not None and not user.is_staff:
            if user.is_active:
                auth.login(request,user)
                return redirect('blog-about')
            else:
                messages.warning(request, 'Account is not active')
                return render(request, 'user_registration/login.html')
        
        else:
            messages.error(request, 'Please enter valid details')
            return render(request, 'user_registration/login.html')

    context = {}
    return render(request, 'user_registration/login.html', context)