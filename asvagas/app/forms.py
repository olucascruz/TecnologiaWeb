from django import forms
from .models import Candidate, Recruiter
from django.contrib.auth.models import User


class RegistrationFormCandidate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
        }

    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    profession = forms.CharField(label="Profissão" , widget=forms.TextInput(attrs={'placeholder':'Engenheiro de Software'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já foi cadastrado.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
                        
        candidate = Candidate.objects.create(user=user, profession=self.cleaned_data['profession'])
        return candidate
    

class RegistrationFormRecruiter(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }

    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    company = forms.CharField(label="Empresa", widget=forms.TextInput(attrs={'placeholder':'Autônomo'}))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já foi cadastrado.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
           user.save()
            
            
        recruiter = Recruiter.objects.create(user=user, company=self.cleaned_data['company'])
        return recruiter
    

class LoginForm(forms.Form):
    error_message = {'required':'Email e Senha necessarios',
                     'invalid':'Email ou Senha incorreto(s)'}
    email = forms.EmailField(error_messages=error_message)
    password = forms.CharField(widget=forms.PasswordInput(), error_messages=error_message)
