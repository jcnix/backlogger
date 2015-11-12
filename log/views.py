from django.shortcuts import render
from django.http import HttpResponse
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
def search_game(request):
	if request.method == 'POST':
		form = GameSearchForm(request.POST)
		#get search results
		if form.is_valid():
			q = form.cleaned_data['query']
			gb = GBApi()
			results = gb.search(q)
	else:
		form = GameSearchForm()
		results = None

	context = {'form': form, 'results': results}
	return render(request, 'log/add_game.html', context)

@login_required
def add_game(request, gbid):
	return HttpResponse(status=200)