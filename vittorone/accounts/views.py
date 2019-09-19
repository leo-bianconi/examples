from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NameForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('market:index')

    elif request.method == 'GET':
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(request.POST.get('next'))

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', { 'form':form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('market:index')
