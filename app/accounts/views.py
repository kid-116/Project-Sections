from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import AccountSignupForm, AccountAuthenticationForm, AccountUpdateForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup_account(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = AccountSignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('walls:orgs_path')
    else:    
        form = AccountSignupForm()
    return render(request, "accounts/signup.html", { 'form': form })


def logout_account(request):
    logout(request)
    return redirect('homepage_path')


def login_account(request):
    user = request.user
    if user.is_authenticated:
        return redirect('walls:orgs_path')
    if request.method == "POST":
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('walls:orgs_path')
    else:
        form = AccountAuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })


@login_required(login_url="/accounts/login")
def update_account(request):
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile updated successfully')
            return redirect('walls:orgs_path')
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
            }
        )
    return render(request, 'accounts/update.html', {
        'form': form,
    })
