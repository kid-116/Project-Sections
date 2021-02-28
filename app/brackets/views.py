from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BracketCreationForm
from django.http import HttpResponse
from brackets.models import Bracket, JoinRequest
from organisations.models import Organisation


@login_required(login_url="/accounts/login/")
def create(request, id_o):
    user = request.user
    if not user.is_staff:
        raise PermissionError
    if request.method == "POST":
        form = BracketCreationForm(request.POST)
        if form.is_valid():
            bracket = form.save(commit=False)
            bracket.organisation = Organisation.objects.get(id=id_o)
            bracket.save()
            return redirect('organisations:home_path', id_o=id_o)
    else:
        form = BracketCreationForm()
    return render(request, 'brackets/create.html', {
        'form': form,
        'id_o': id_o
    })

@login_required(login_url="/accounts/login/")
def home(request, id_b):
    user = request.user
    bracket = Bracket.objects.get(id=id_b)
    if user.belong_to.filter(id=bracket.organisation.id) and (user.is_staff or (user == bracket.cr) or (user == bracket.faculty_advisor)):
        return render(request, 'brackets/home.html', {
            'bracket': bracket,
            'joinreqs': bracket.join_requests.filter(accepted=None)
        })
@login_required(login_url="/accounts/login/")
def index(request, id_o):
    if request.user.belong_to.filter(id=id_o).exists():
        sections = Organisation.objects.get(id=id_o).brackets.exclude(id__in=request.user.brackets.all().values('id'))
        return render(request, 'brackets/index.html', { 'sections': sections })
    else:
        raise PermissionError

@login_required(login_url="/accounts/login")
def create_joinreq(request, id_b):
    id_o = Bracket.objects.get(id=id_b).organisation.id
    if request.user.belong_to.filter(id=id_o).exists():
        if not JoinRequest.objects.filter(
        account=request.user,
        bracket=Bracket.objects.get(id=id_b),
        accepted=None).exists():
            joinreq = JoinRequest(
            account=request.user,
            bracket=Bracket.objects.get(id=id_b),
            )
            joinreq.save()
        return redirect('brackets:index_path', id_o=id_o)
    else:
        raise PermissionError

def accept_joinreq(request, id_r):
    req = JoinRequest.objects.get(id=id_r)
    req.accepted = True
    req.bracket.members.add(req.account)
    req.save()
    return redirect('brackets:home_path', id_b=req.bracket.id)

def decline_joinreq(request, id_r):
    req = JoinRequest.objects.get(id=id_r)
    req.accepted = False
    req.save()
    return redirect('brackets:home_path', id_b=req.bracket.id)

