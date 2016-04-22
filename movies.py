import requests
from left_pad import left_pad
# api_key = uncommment and inesrt your api key here

response = requests.get('https://api.themoviedb.org/3/discover/tv',
	{'sort_by': 'popularity.desc', 'api_key': api_key})

#Parse the json repsonse
movies = response.json()

for movie in movies['results']:
	print (left_pad(movie['name'], 40) + ' ' + '*' * int(movie['popularity'] / 2))
