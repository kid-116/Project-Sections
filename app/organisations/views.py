from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Organisation, JoinRequest
from django.contrib import messages


@login_required(login_url="/accounts/login/")
def register(request):
    if request.method == "POST":
        form = forms.NewOrganisationForm(request.POST, request.FILES)
        if form.is_valid():
            organisation = form.save()
            organisation.members.add(request.user)
            organisation.admins.add(request.user)
            organisation.save()
            messages.add_message(request, messages.SUCCESS, 'Organisation registration successful')
            messages.add_message(request, messages.INFO, 'Please wait for onboarding to be accepted')
            return redirect('homepage_path')
    else:
        form = forms.NewOrganisationForm()
    return render(request, 'organisations/register.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def index_regreqs(request):
    if request.user.is_superuser:
        reg_requests = Organisation.objects.all().filter(is_activated=None)
        return render(request, 'organisations/reg-reqs.html', { 'reg_requests': reg_requests })
    else:
        raise PermissionError

@login_required(login_url="/accounts/login")
def accept_regreq(request, id_o):
    if request.user.is_superuser:
        org = Organisation.objects.get(id=id_o)
        org.is_activated = True
        org.save()
        return redirect('organisations:index_regreqs_path')
    else:
        raise PermissionError

@login_required(login_url="/accounts/login")
def decline_regreq(request, id_o):
    if request.user.is_superuser:
        org = Organisation.objects.get(id=id_o)
        org.is_activated = False
        org.save()
        return redirect('organisations:index_regreqs_path')
    else:
        raise PermissionError

@login_required(login_url="/accounts/login")
def home(request, id_o):
    if request.user.admin_of.filter(id=id_o).exists():
        org = Organisation.objects.get(id=id_o)
        user_brackets = request.user.brackets.filter(id=id_o)
        is_orgadmin = org.admins.filter(username=request.user.username).exists()
        return render(request, 'organisations/home.html', {
            'org': org,
            'user_brackets': user_brackets,
            'is_orgadmin': is_orgadmin
        }) 
    else:
        raise PermissionError

@login_required(login_url="/accounts/login")
def accept_joinreq(request, id_o, id_j):
    if request.user.admin_of.filter(id=id_o).exists():
        req = JoinRequest.objects.get(id=id_j)
        req.org.members.add(req.account)
        req.accepted = True
        req.save()
        return redirect('organisations:home_path', id_o=id_o)
    else:
        raise PermissionError

@login_required(login_url="/accounts/login")
def decline_joinreq(request, id_o, id_j):
    if request.user.admin_of.filter(id=id_o).exists():
        req = JoinRequest.objects.get(id=id_j)
        req.accepted = False
        req.save()
        return redirect('organisations:home_path', id_o=id_o)
    else:
        raise PermissionError

@login_required(login_url="/accounts/login")
def joinreq(request):
    if request.method == "POST":
        form = forms.JoinRequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.account = request.user
            req.save()
            return redirect('walls:home_path')
    else:
        form = forms.JoinRequestForm()
    return render(request, 'organisations/join.html', {
        'form': form,
    })

@login_required(login_url="/accounts/login")
def admin_page(request, id_o):
    user = request.user
    is_org_admin = user.admin_of.filter(id=id_o).exists()
    if is_org_admin:
        org = Organisation.objects.get(id=id_o)
        return render(request, 'organisations/admin_page.html', {
            'org': org,
        })
    else:
        raise PermissionError





