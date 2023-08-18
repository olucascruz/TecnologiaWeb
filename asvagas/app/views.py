from django.shortcuts import render
# Create your views here.
from .forms import *

def index(request):
    return render(request, "templates/index.html")

def login(request):
    return render(request, "templates/login.html")

def register(request):
    form_candidate = RegistrationFormCandidate()
    form_recruiter = RegistrationFormRecruiter()
    return render(request, "templates/register.html",{'form_candidate':form_candidate, 'form_recruiter':form_recruiter})