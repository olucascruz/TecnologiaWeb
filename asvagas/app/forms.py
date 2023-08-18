from django import forms
from .models import Candidate, Recruiter

class RegistrationFormCandidate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Candidate
        fields = ['name', 'email', 'password', 'profession']

class RegistrationFormRecruiter(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Recruiter
        fields = ['name', 'email', 'password', 'company']