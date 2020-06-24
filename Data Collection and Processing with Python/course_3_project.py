1.# Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

# # Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The 
# function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be 
# a python dictionary with just one key, ‘Similar’.

# # Try invoking your function with the input “Black Panther”.

# # HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then 
# the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to
#  complete the project, because all data will be found in the cache.

# # some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# # get_movies_from_tastedive("Bridesmaids")
# # get_movies_from_tastedive("Black Panther")

import requests_with_caching
import json

def get_movies_from_tastedive(movieName):
    baseUrl = "https://tastedive.com/api/similar"
    param_dic = {}
    param_dic["q"] = movieName
    param_dic["type"] = "movies"
    param_dic["limit"] = 5
    movie_resp = requests_with_caching.get(baseUrl, params = param_dic)
    #py_data = json.loads(movie_resp.text)
    return movie_resp.json()

print(get_movies_from_tastedive("Bridesmaids"))



2.
# Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list
# of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
import requests_with_caching
import json

def get_movies_from_tastedive(movieName):
    baseUrl = "https://tastedive.com/api/similar"
    param_dic = {}
    param_dic["q"] = movieName
    param_dic["type"] = "movies"
    param_dic["limit"] = 5
    movie_resp = requests_with_caching.get(baseUrl, params = param_dic)
    return movie_resp.json()
print(get_movies_from_tastedive("Captain Marvel"))

def extract_movie_titles(movieList):
    movie_list = []
    for movie in movieList["Similar"]["Results"]:
        movie_list.append(movie["Name"])
    return movie_list

print(extract_movie_titles(get_movies_from_tastedive("Black Panther")))



 3
 # .Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called 
# get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles
# for all of them, and combines them all into a single list. Don’t include the same movie twice.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])
import requests_with_caching
import json

def get_movies_from_tastedive(movieName):
    baseUrl = "https://tastedive.com/api/similar"
    param_dic = {}
    param_dic["q"] = movieName
    param_dic["type"] = "movies"
    param_dic["limit"] = 5
    movie_resp = requests_with_caching.get(baseUrl, params = param_dic)
    return movie_resp.json()
#print(get_movies_from_tastedive("Captain Marvel"))
def extract_movie_titles(movieList):
    movie_list = []
    for movie in movieList["Similar"]["Results"]:
        movie_list.append(movie["Name"])
    return movie_list
#print(extract_movie_titles(get_movies_from_tastedive("Captain Marvel")))
def get_related_titles(movieTitleList):
    movie_title_list = []
    for item in range(len(movieTitleList)):
        movieTitle = movieTitleList[item]
        movieList1 = extract_movie_titles(get_movies_from_tastedive(movieTitle))
        print(len(movieList1))
        #print(movieList1)
        c = 0
        while c < 5:
            if movieList1[c] not in movie_title_list:
                movie_title_list.append(movieList1[c])
            c += 1
    return movie_title_list
A = get_related_titles(["Black Panther", "Captain Marvel"])
print(A)
print(len(A))


4. 
# Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
# Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you
# want to search. The function should return a dictionary with information about that movie.

# Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will 
# need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract
# existing data from the cache.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import requests_with_caching
import json 

def get_movie_data(movieTitle):
    baseUrl = "http://www.omdbapi.com/"
    movieInfo = {}
    movieInfo["t"] = movieTitle
    movieInfo["r"] = 'json'
    M = requests_with_caching.get(baseUrl, params = movieInfo)
    return M.json()
    
print(get_movie_data("Baby Mama"))

5.
# Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an 
# OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for 
# “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#
import requests_with_caching
import json 

def get_movie_data(movieTitle):
    baseUrl = "http://www.omdbapi.com/"
    movieInfo = {}
    movieInfo["t"] = movieTitle
    movieInfo["r"] = 'json'
    M = requests_with_caching.get(baseUrl, params = movieInfo)
    return M.json()
def get_movie_rating(omdbDict):
    score = 0
    for item in omdbDict["Ratings"]:
        if item["Source"] == 'Rotten Tomatoes':
            score = int(item['Value'][:-1])
    return score
A = get_movie_rating(get_movie_data("Deadpool 2"))
print(A)



6.
# Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window.
# Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles
# as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating,
# as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.


import requests_with_caching
import json


def get_movies_from_tastedive(movieName):
    baseUrl = "https://tastedive.com/api/similar"
    param_dic = {}
    param_dic["q"] = movieName
    param_dic["type"] = "movies"
    param_dic["limit"] = 5
    movie_resp = requests_with_caching.get(baseUrl, params=param_dic)
    return movie_resp.json()


# print(get_movies_from_tastedive("Captain Marvel"))
def extract_movie_titles(movieList):
    movie_list = []
    for movie in movieList["Similar"]["Results"]:
        movie_list.append(movie["Name"])
    return movie_list


# print(extract_movie_titles(get_movies_from_tastedive("Captain Marvel")))
def get_related_titles(movieTitleList):
    movie_title_list = []
    for item in range(len(movieTitleList)):
        movieTitle = movieTitleList[item]
        movieList1 = extract_movie_titles(get_movies_from_tastedive(movieTitle))
        c = 0
        while c < 5:
            if movieList1[c] not in movie_title_list:
                movie_title_list.append(movieList1[c])
            c += 1
    print(movie_title_list)
    return movie_title_list
# A = get_related_titles(["Black Panther", "Captain Marvel"])
#print(A)


def get_movie_data(movieTitle):
    baseUrl = "http://www.omdbapi.com/"
    movieInfo = {}
    movieInfo["t"] = movieTitle
    movieInfo["r"] = 'json'
    M = requests_with_caching.get(baseUrl, params=movieInfo)
    return M.json()

def get_movie_rating(omdbDict):
    score = 0
    for item in omdbDict["Ratings"]:
        if item["Source"] == 'Rotten Tomatoes':
            score = int(item['Value'][:-1])
            #print(score)
    return score


def get_sorted_recommendations(mvList):
    movieList = get_related_titles(mvList)
    sortestMovieList = []
    print(movieList)
    M1 = movieList[0]
    print(M1)
    print(get_movie_rating(get_movie_data(M1)))
    
   # for item in range(len(movieList)):
    #    if 
    return sortestMovieList


cc = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])




