from django import forms
from .models import Candidate, Recruiter

class RegistrationFormCandidate(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    profession = forms.CharField(label="Profissão" , widget=forms.TextInput(attrs={'placeholder':'Engenheiro de Software'}))

    class Meta:
        model = Candidate
        fields = ['name', 'email', 'password', 'profession']
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
        }

class RegistrationFormRecruiter(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    company = forms.CharField(label="Empresa", widget=forms.TextInput(attrs={'placeholder':'Autônomo'}))
    class Meta:
        model = Recruiter
        fields = ['name', 'email', 'password', 'company']
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'password': 'Senha',
            'company': 'Empresa',
        }

class LoginForm(forms.Form):
    error_message = {'error':'Email ou Senha incorreto(s)'}
    email = forms.EmailField(error_messages=error_message)
    password = forms.CharField(widget=forms.PasswordInput(), error_messages=error_message)
