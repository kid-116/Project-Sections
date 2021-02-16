from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BracketCreationForm
from django.http import HttpResponse
from brackets.models import Bracket
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

# @login_required(login_url="/accounts/login/")
# def index(request):
#     user = request.user
#     if not user.is_staff:
#         return HttpResponse('Access Denied!')
#     return render(request, 'brackets/index.html')

# @login_required(login_url="/accounts/login/")
# def join(request):
#     if request.method == "POST":
#         form = JoinRequestCreationForm(request.POST)
#         if form.is_valid():
#             join_req = form.save(commit=False)
#             join_req.account = request.user
#             join_req.slug = join_req.account.username+'-'+ join_req.bracket.name
#             join_req.save()
#         return redirect('walls:wall_path')
#     else:
#         form = JoinRequestCreationForm()
#     return render(request, 'brackets/join.html', { 'form': form })

# @login_required(login_url="/accounts/login")
# def index_joinreqs(request):
#     if request.user.is_staff or request.user.cr_of.all().exists() or request.user.facadv_of.all().exists():
#         sections = request.user.brackets.all()
#         return render(request, 'brackets/index_joinreqs.html', { 'sections': sections })
#     else:
#         raise PermissionError

# def accept_join_req(request, id):
#     req = JoinRequest.objects.get(id=id)
#     req.accepted = True
#     # Add to section
#     req.bracket.members.add(req.account)
#     req.is_active = False
#     req.save()
#     return redirect('brackets:index_joinreqs_path')

# def decline_join_req(request, id):
#     req = JoinRequest.objects.get(id=id)
#     req.accepted = False
#     req.is_active = False
#     req.save()
#     return redirect('brackets:index_joinreqs_path')

