from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url="/accounts/login/")
def orgs_wall(request):
    orgs = request.user.belong_to.all().order_by('date_created')
    return render(request, 'walls/my_orgs.html', {
        'orgs': orgs
    })