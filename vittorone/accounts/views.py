from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm, UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', { 'form': form })
