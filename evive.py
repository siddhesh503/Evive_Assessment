import requests
import calendar;
import time;
from collections import Counter
from utils import utils

starting_time = calendar.timegm(time.gmtime())
########################################getting movie list#####################################################
movie_id_list = utils.get_total_media_ids(["primary_release_date.gte","primary_release_date.lte"],"movie")
movie_id_list = list(movie_id_list)
print(len(movie_id_list))
#############################getting cast for movies##############################################
cast_id_list = utils.get_total_cast_ids("movie",movie_id_list)
cast_id_list = list(cast_id_list)
print(len(cast_id_list))
####################################################getting tv show list######################################
tv_id_list = utils.get_total_media_ids(["air_date.gte","air_date.lte"],"tv")
tv_id_list = list(tv_id_list)
print(len(tv_id_list))
######################################################getting tv cast######################################
cast_id_list_tv = utils.get_total_cast_ids("tv",tv_id_list)
cast_id_list_tv = list(cast_id_list_tv)
###########################################showing results!!#################################################3
print('------------------------------ count is -----------------------------------')
print(len(set(cast_id_list_tv).intersection(set(cast_id_list))))
print('--------------------------execution time is-----------------------------')
print((calendar.timegm(time.gmtime())-starting_time)/60,":Mins")
