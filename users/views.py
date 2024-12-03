from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages


def profile_view(request):
    profile = request.user.profile
    context = {
        'profile' : profile
    }
    return render(request,'users/profile.html',context)


def profile_edit_view(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid(): 
            form.save()
            return redirect('profile')
    context = {
        'form' : form
    }
    return render(request,'users/profile_edit.html',context)