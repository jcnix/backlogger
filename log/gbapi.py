from django.conf import settings
import urllib2
import json

class GBApi:
	def __init__(self):
		self.api_key = settings.GB_API_KEY
		self.gb_url = 'http://www.giantbomb.com/api'

	def search(self, query):
		request = self.gb_url+'/search/?query='+query+'&api_key='+self.api_key+'&resources=game&field_list=name,image&format=json'
		response = urllib2.urlopen(request)
		r = response.read()
		j = json.loads(r)
		return j['results']