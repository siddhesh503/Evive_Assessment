import requests
import calendar;
import time;
from collections import Counter
from utils import utils

starting_time = calendar.timegm(time.gmtime())
########################################getting movie list#####################################################33
page_number = 1
response_dict = utils.get_media_ids(page_number,"movie",["primary_release_date.gte","primary_release_date.lte"])
page_number += 1
movie_id_list = response_dict['id_set']
X_RateLimit_Reset = response_dict['X_RateLimit_Reset']
X_RateLimit_Remaining = response_dict['X_RateLimit_Remaining']
total_pages = response_dict['total_pages']

"""
TMDB allows to access only 1000 pages
here is the reference on their official website:
https://www.themoviedb.org/talk/590ca6eac3a36865190008be?language=en
"""

while page_number <= total_pages and page_number <=1000 :
	if X_RateLimit_Remaining == 0:
		try:
			print('------------------inside delay---------------')
			print(X_RateLimit_Reset)
			print(calendar.timegm(time.gmtime()))
			time.sleep(X_RateLimit_Reset - calendar.timegm(time.gmtime())+1) #adding 0.5 seconds is just to add a buffer in case of any 
			print(calendar.timegm(time.gmtime()))
			X_RateLimit_Remaining = 1 # assigning any non zero value to make the for loop go forward and to not enter this if block again unless necessary
		except Exception as e:
			print(e)
			page_number += 1
	else:
		response_dict = utils.get_media_ids(page_number,"movie",["primary_release_date.gte","primary_release_date.lte"])
		page_number += 1
		id_set = response_dict['id_set']
		movie_id_list = movie_id_list.union(id_set)
		X_RateLimit_Reset = response_dict['X_RateLimit_Reset']
		X_RateLimit_Remaining = response_dict['X_RateLimit_Remaining']

print(len(movie_id_list))
movie_id_list = list(set(movie_id_list))
print(len(movie_id_list))

#############################getting cast for movies##############################################

response_dict = utils.get_cast_ids("movie",movie_id_list[0])
cast_id_list = response_dict["id_set"]
print(cast_id_list)
X_RateLimit_Reset = response_dict["X_RateLimit_Reset"] 
X_RateLimit_Remaining = response_dict["X_RateLimit_Remaining"] 
counter = 1

while counter < len(movie_id_list) :
	if X_RateLimit_Remaining == 0:
		try:
			print('------------------inside delay---------------')
			print(X_RateLimit_Reset)
			print(calendar.timegm(time.gmtime()))
			time.sleep(X_RateLimit_Reset - calendar.timegm(time.gmtime())+1) #adding 1 second is just to add a buffer in case of any 
			print(calendar.timegm(time.gmtime()))
			X_RateLimit_Remaining = 1 # assigning any non zero value to make the for loop go forward and to not enter this if block again unless necessary
		except Exception as e:
			print(e)
			counter+=1
	else:
		response_dict = utils.get_cast_ids("movie",movie_id_list[counter])
		id_set = response_dict["id_set"]
		cast_id_list = cast_id_list.union(id_set)
		X_RateLimit_Reset = response_dict["X_RateLimit_Reset"] 
		X_RateLimit_Remaining = response_dict["X_RateLimit_Remaining"]
		print(counter) 
		counter+=1

cast_id_list = list(set(cast_id_list))
print(len(cast_id_list))

####################################################getting tv show list######################################
page_number = 1
response_dict = utils.get_media_ids(page_number,"tv",["air_date.gte","air_date.lte"])
page_number += 1
tv_id_list = response_dict['id_set']
X_RateLimit_Reset = response_dict['X_RateLimit_Reset']
X_RateLimit_Remaining = response_dict['X_RateLimit_Remaining']
total_pages = response_dict['total_pages']

"""
TMDB allows to access only 1000 pages
here is the reference on their official website:
https://www.themoviedb.org/talk/590ca6eac3a36865190008be?language=en
"""

while page_number <= total_pages and page_number <=1000 :
	if X_RateLimit_Remaining == 0:
		try:
			print('------------------inside delay---------------')
			print(X_RateLimit_Reset)
			print(calendar.timegm(time.gmtime()))
			time.sleep(X_RateLimit_Reset - calendar.timegm(time.gmtime())+1) #adding 0.5 seconds is just to add a buffer in case of any 
			print(calendar.timegm(time.gmtime()))
			X_RateLimit_Remaining = 1 # assigning any non zero value to make the for loop go forward and to not enter this if block again unless necessary
		except Exception as e:
			print(e)
			page_number += 1
	else:
		response_dict = utils.get_media_ids(page_number,"tv",["air_date.gte","air_date.lte"])
		page_number += 1
		id_set = response_dict['id_set']
		tv_id_list = tv_id_list.union(id_set)
		X_RateLimit_Reset = response_dict['X_RateLimit_Reset']
		X_RateLimit_Remaining = response_dict['X_RateLimit_Remaining']


print(len(tv_id_list))
tv_id_list = list(set(tv_id_list))
print(len(tv_id_list))

######################################################getting tv cast######################################
response_dict = utils.get_cast_ids("tv",tv_id_list[0])
cast_id_list_tv = response_dict["id_set"]
print(cast_id_list_tv)
X_RateLimit_Reset = response_dict["X_RateLimit_Reset"] 
X_RateLimit_Remaining = response_dict["X_RateLimit_Remaining"] 
counter = 1

while counter < len(tv_id_list) :
	if X_RateLimit_Remaining == 0:
		try:
			print('------------------inside delay---------------')
			print(X_RateLimit_Reset)
			print(calendar.timegm(time.gmtime()))
			time.sleep(X_RateLimit_Reset - calendar.timegm(time.gmtime())+1) #adding 1 second is just to add a buffer in case of any 
			print(calendar.timegm(time.gmtime()))
			X_RateLimit_Remaining = 1 # assigning any non zero value to make the for loop go forward and to not enter this if block again unless necessary
		except Exception as e:
			print(e)
			counter+=1
	else:
		response_dict = utils.get_cast_ids("tv",tv_id_list[counter])
		id_set = response_dict["id_set"]
		cast_id_list_tv = cast_id_list_tv.union(id_set)
		X_RateLimit_Reset = response_dict["X_RateLimit_Reset"] 
		X_RateLimit_Remaining = response_dict["X_RateLimit_Remaining"]
		print(counter) 
		counter+=1


cast_id_list_tv = list(set(cast_id_list_tv))
print('------------------------------ count is -----------------------------------')
print(len(set(cast_id_list_tv).intersection(set(cast_id_list))))
print('--------------------------execution time is-----------------------------')
print((calendar.timegm(time.gmtime())-starting_time)/60,":Mins")
