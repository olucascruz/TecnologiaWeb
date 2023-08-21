from django.shortcuts import render
# Create your views here.
from .forms import *

def index(request):
    return render(request, "templates/index.html")

def login(request):
    form_login = LoginForm()
    context = {'form_login':form_login}
    
    return render(request, "templates/login.html", context=context )

def register(request):
    form_candidate = RegistrationFormCandidate()
    form_recruiter = RegistrationFormRecruiter()
    context = {'form_candidate':form_candidate,
               'form_recruiter':form_recruiter}
    
    return render(request, "templates/register.html", context=context)