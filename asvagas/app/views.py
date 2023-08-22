from django.shortcuts import render, redirect
# Create your views here.
from .forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import *

@login_required(login_url='/login')
def home(request):
    return render(request, 'templates/home.html')

def login(request):
    if request.method == "POST":
        print("aaaaaaaaaaaaa")
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(email=email)
            
            if user.check_password(password):
                print(user.password)
                auth_login(request, user)
        except Exception as err: print(err) 
        
        
        return redirect("home")
    else:
        form_login = LoginForm()
        context = {'form_login':form_login}

        return render(request, "templates/login.html", context=context )

def register(request):

    form_candidate = RegistrationFormCandidate()
    form_recruiter = RegistrationFormRecruiter()
    context = {'form_candidate':form_candidate,
               'form_recruiter':form_recruiter}
    if request.method == "POST":
        if 'profession' in request.POST:
            form = RegistrationFormCandidate(request.POST)
        else:
            form = RegistrationFormRecruiter(request.POST)
        
        
        if form.is_valid():    
            form.save()
            
        else:
            if 'profession' in request.POST:
                context['form_candidate'] = form
            else:
                context['form_recruiter'] = form
            
            return render(request, "templates/register.html", context=context)

            
        return redirect('login')
    else:    
        
        
        return render(request, "templates/register.html", context=context)
    
def logout(request):
    auth_logout(request)
    return redirect("login")