from django import forms

class GameSearchForm(forms.Form):
	query = forms.CharField()