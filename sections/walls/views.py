from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url="/accounts/login/")
def wall(request):
    user = request.user
    if user.role == 'S':
        return render(request, 'walls/student.html')
    elif user.role == 'T':
        return render(request, 'walls/teacher.html')
    elif user.is_superuser:
        return redirect('/admin/')
    elif user.is_staff:
        return redirect('walls/administrator.html')

@login_required(login_url="/accounts/login/")
def administrator_wall(request):
    if request.user.is_staff:
        orgs = request.user.belong_to.all()
        return render(request, 'walls/administrator.html', {
            'orgs': orgs
        })
    else:
        raise PermissionError