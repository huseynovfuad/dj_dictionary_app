from django import forms
from .models import MyUser
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username','password1','password2',]

    def clean(self,*args,**kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise forms.ValidationError("Passwords should match")
        return super(RegistrationForm,self).clean(*args,**kwargs)



class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ['username','password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username,password=password):
            raise forms.ValidationError("Email or Password is wrong")