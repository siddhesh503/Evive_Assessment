import requests
import calendar;
import time;
from collections import Counter

######################################## utility functions##############################################
def get_media_ids(page_number,media_type,query_params):
	try:
		base_url = "http://api.themoviedb.org/3/discover/{}?{}=2017-12-01&{}=2017-12-31&api_key=606aaffd7ca10f0b80804a1f0674e4e1"
		url = base_url.format(media_type,query_params[0],query_params[1]) + "&page=" + str(page_number)
		response = requests.get(url, headers={'User-Agent':'my agent'})
		response_json =response.json()
		results = response_json['results']
		total_pages = response_json['total_pages']
		print(response.headers)
		print(page_number)
		id_set = set()
		for result_dict in results:
			try:
				id_set.add(result_dict["id"])            ######sometimes results have null objects
			except Exception as e:
				print(e)
		X_RateLimit_Reset = int(response.headers['X-RateLimit-Reset'])
		X_RateLimit_Remaining = int(response.headers['X-RateLimit-Remaining'])
		return ({'id_set':id_set,'X_RateLimit_Reset':X_RateLimit_Reset,'X_RateLimit_Remaining':X_RateLimit_Remaining,'total_pages':total_pages})
	except Exception as e:
			print(e)
			default_set = set()
			return ({'id_set':default_set,'X_RateLimit_Reset': 1,'X_RateLimit_Remaining':calendar.timegm(time.gmtime())})    ###default dict to keep program running

def get_cast_ids(media_type,media_id):
	try:
		base_url = "https://api.themoviedb.org/3/{}/{}/credits?api_key=606aaffd7ca10f0b80804a1f0674e4e1"
		url = base_url.format(media_type,media_id)
		response = requests.get(url, headers={'User-Agent':'my agent'})
		response_json =response.json()
		cast_list = response_json['cast']
		id_set = set()
		for cast_dict in cast_list:
			try:
				id_set.add(cast_dict["id"])            ######sometimes results have null objects
			except Exception as e:
				print(e)
		X_RateLimit_Reset = int(response.headers['X-RateLimit-Reset'])
		X_RateLimit_Remaining = int(response.headers['X-RateLimit-Remaining'])
		return ({'id_set':id_set,'X_RateLimit_Reset':X_RateLimit_Reset,'X_RateLimit_Remaining':X_RateLimit_Remaining})
	except Exception as e:
		print(e)
		default_set = set()
		return ({'id_set':default_set,'X_RateLimit_Reset': 1,'X_RateLimit_Remaining':calendar.timegm(time.gmtime())})    ###default dict to keep program running
