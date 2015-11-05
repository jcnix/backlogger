from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
	context = {'nbar': 'home'}
	return render(request, 'log/index.html', context)

@login_required
def profile(request):
	context = {'username': request.user.username, 'nbar': 'profile'}
	return render(request, 'accounts/profile.html', context)

@login_required
def add_game(request):
	context = {}
	return render(request, 'log/add_game.html', context)