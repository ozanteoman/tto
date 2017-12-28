from django.shortcuts import render
from .forms import UserCreateForm,UserLoginForm
from django.contrib.auth.views import login,logout
from django.contrib.auth import authenticate
from django.shortcuts import reverse,HttpResponseRedirect

def user_create(request):
    user_create_form = UserCreateForm()
    if request.method == "POST":
        user_create_form=UserCreateForm(request.POST)
        user=user_create_form.save(commit=False)
        password = user_create_form.cleaned_data['password']
        username = user_create_form.cleaned_data['username']
        user.set_password(password)
        user.save()
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('post-list'))
    return render(request,'users/user-create.html',context={'form':user_create_form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('post-list'))

def user_login(request):
    user_form = UserLoginForm()
    if request.method == "POST":
        user_form=UserLoginForm(data=request.POST)
        if user_form.is_valid():
            password = user_form.cleaned_data['password']
            username = user_form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request,user)
            return HttpResponseRedirect(reverse('post-list'))

    return render(request,'users/user-login.html',context={'form':user_form})
