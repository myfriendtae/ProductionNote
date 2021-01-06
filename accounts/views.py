from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.conf import settings
from django.http import HttpResponseRedirect

from .forms import LoginForm
from django.core.mail import EmailMessage

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        login_form = LoginForm()
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        if request.method == 'POST':
            login_form = LoginForm(request=request, data=request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.session['login_from'])
            else:
                messages.error(request, 'Email OR Password is incorrect.')
        context = {'login_form': login_form}
        return render(request, 'accounts/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('accounts:login_page')

def login_required(request):
    login_form = LoginForm()
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        login_form = LoginForm(request=request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.session['login_from'])
        else:
            messages.error(request, 'Email OR Password is incorrect.')
    context = {'login_form': login_form}
    return render(request, 'accounts/login_required.html', context)