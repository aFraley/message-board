from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('topics:topic-list'))
        else:
            return render(request, 'accounts/login.html', {
                "is_error": True,
                "error": "Invalid password and/or username."
            })
    return render(request, 'accounts/login.html')


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('posts:post-list'))
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {
        'form': form
    })


@login_required(login_url='accounts/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


@login_required(login_url='accounts/login/')
def profile_view(request):
    return render(request, 'accounts/profile.html')

