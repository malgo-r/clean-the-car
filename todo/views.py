from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm


def signupuser(request):
    return render(request, template_name='todo/signupuser.html', context={'form': UserChangeForm()})
