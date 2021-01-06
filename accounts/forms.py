from django.forms import PasswordInput, TextInput, CharField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder': 'Username'}), required=True)
    password = CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}), required=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]