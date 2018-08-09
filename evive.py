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

movie_id_list = utils.get_total_media_ids(["primary_release_date.gte","primary_release_date.lte"],"movie",page_number,total_pages,X_RateLimit_Remaining,X_RateLimit_Reset,movie_id_list)

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

cast_id_list = utils.get_total_cast_ids("movie",counter,movie_id_list,X_RateLimit_Remaining,X_RateLimit_Reset,cast_id_list)

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


tv_id_list = utils.get_total_media_ids(["air_date.gte","air_date.lte"],"tv",page_number,total_pages,X_RateLimit_Remaining,X_RateLimit_Reset,tv_id_list)



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


cast_id_list_tv = utils.get_total_cast_ids("tv",counter,tv_id_list,X_RateLimit_Remaining,X_RateLimit_Reset,cast_id_list_tv)

cast_id_list_tv = list(set(cast_id_list_tv))


###########################################showing results!!#################################################3
print('------------------------------ count is -----------------------------------')
print(len(set(cast_id_list_tv).intersection(set(cast_id_list))))
print('--------------------------execution time is-----------------------------')
print((calendar.timegm(time.gmtime())-starting_time)/60,":Mins")
