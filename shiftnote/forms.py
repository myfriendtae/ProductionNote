from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.forms import CharField, PasswordInput, EmailField, EmailInput
from django.contrib.auth.models import User

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}), required=True)
    new_password2 = CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password confirmation'}), required=True)

    class Meta:
        model = User
        fields = [
            'new_password1',
            'new_password2',
        ]

class CustomPasswordResetForm(PasswordResetForm):
    email = EmailField(widget=EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter email'}), required=True)

    class Meta:
        model = User
        field = [
            'email',
        ]