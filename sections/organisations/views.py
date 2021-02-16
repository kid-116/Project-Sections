from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Organisation, JoinRequest


@login_required(login_url="/accounts/login/")
def create(request):
    if request.method == "POST":
        form = forms.NewOrganisationForm(request.POST)
        if form.is_valid():
            organisation = form.save(commit=False)
            organisation.administrator = request.user
            organisation.save()
            return redirect('homepage_path')
    else:
        form = forms.NewOrganisationForm()
    return render(request, 'organisations/create.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def index_joinreqs(request):
    if request.user.is_superuser:
        join_requests = Organisation.objects.all().filter(is_activated=None)
        return render(request, 'organisations/join-reqs.html', { 'join_requests': join_requests })
    else:
        raise PermissionError

def accept_joinreq(request, id):
    org = Organisation.objects.get(id=id)
    org.is_activated = True
    org.save()
    user = org.administrator
    org.members.add(user)
    user.is_staff = True
    user.save()
    return redirect('organisations:index_joinreqs_path')

def decline_joinreq(request, id):
    org = Organisation.objects.get(id=id)
    org.is_activated = False
    org.save()
    return redirect('organisations:index_joinreqs_path')

@login_required(login_url="/accounts/login")
def home(request, id_o):
    if request.user.is_staff:
        org = Organisation.objects.get(id=id_o)
        joinreqs = org.joinreqs.all().filter(accepted=None)
        return render(request, 'organisations/home.html', {
            'org': org,
            'joinreqs': joinreqs
        }) 
    else:
        raise PermissionError

def accept_user_joinreq(request, id_o, id_j):
    req = JoinRequest.objects.get(id=id_j)
    req.org.members.add(req.account)
    req.accepted = True
    req.save()
    return redirect('organisations:home_path', id_o=id_o)

def decline_user_joinreq(request, id_o, id_j):
    req = JoinRequest.objects.get(id=id_j)
    req.accepted = False
    req.save()
    return redirect('organisations:home_path', id_o=id_o)

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





