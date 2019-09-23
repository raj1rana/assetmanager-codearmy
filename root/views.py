from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Login import views

# Create your views here.

@login_required

def UserHome(request):
    if request.user.is_authenticated:
        return render(request, 'root/index.html')
    else:
        views.user_login(request)
