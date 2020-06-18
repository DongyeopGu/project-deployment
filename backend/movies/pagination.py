genre_list = {
    	'Adventure': 12,
    	'Fantasy': 14,
    	'Animation': 16,
    	'Drama': 18,
    	'Horror': 27,
    	'Action': 28,
    	'Comedy': 35,
    	'History': 36,
    	'Western': 37,
		'Romance': 10749,
    	'Thriller': 53,
    	'Crime': 80,
    	'Documentary': 99,
    	'ScienceFiction': 878,
    	'Mystery': 9648,
    	'Music': 10402,
    	'Family':10751,
    	'War': 10752,
    	'TVmovie': 10770
}

def genre_movie_list(genre_name):
    return genre_list[genre_name]
