from django.shortcuts import render, redirect


def homepage(request):
    if request.user.is_authenticated:
        return redirect('walls:orgs_path')
    else:
        return render(request, 'homepage.html')