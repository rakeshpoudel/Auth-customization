from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    contactNo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email','password','password_2','contactNo',]
