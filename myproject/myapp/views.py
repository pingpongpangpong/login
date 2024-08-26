# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'login.html')

@login_required
def home(request):
	user = request.user
	context = {
		'username': user.username,
		'email': user.email,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'42_id': user.social_auth.get(provider='42').uid,
	}
	return render(request, 'home.html', context)

def logout_view(request):
    auth_logout(request)
    return redirect('/')
