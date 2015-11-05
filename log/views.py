from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import GameSearchForm
from .gbapi import GBApi

def index(request):
	context = {'nbar': 'home'}
	return render(request, 'log/index.html', context)

@login_required
def profile(request):
	context = {'username': request.user.username, 'nbar': 'profile'}
	return render(request, 'accounts/profile.html', context)

@login_required
def add_game(request):
	form = GameSearchForm()
	results = None
	if request.method == 'POST':
		form = GameSearchForm(request.POST)
		#get search results
		if form.is_valid():
			q = form.cleaned_data['query']
			gb = GBApi()
			results = gb.search(q)

	context = {'form': form, 'results': results}
	return render(request, 'log/add_game.html', context)