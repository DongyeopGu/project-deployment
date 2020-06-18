import requests
import json
import random
from collections import OrderedDict
from backend.settings import TMDB_API_KEY

api_key = TMDB_API_KEY
# movie_list = range(2000)

# movie_list = range(5)
def tmdb_search(search, word, page=1):
    URL = f"https://api.themoviedb.org/3/search/{search}?api_key={api_key}&language=ko&query={word}&page={page}"

    response = requests.get(URL)
    if response.status_code == 200:
        data = json.loads(response.text)
        # for i in range(len(data['results'])):
        #     file_data = OrderedDict()
        #     file_data["model"] = "movies.movie"
        #     file_data["pk"] = data['results'][i]["id"]
        #     file_data["fields"] = dict()
        #     file_data["fields"]["adult"] = data['results'][i]["adult"]
        #     file_data["fields"]["backdrop_path"] = data['results'][i]["backdrop_path"]
        #     file_data["fields"]["genres"] = list()
        #     for j in range(len(data['results'][i]["genre_ids"])):
        #         file_data["fields"]["genres"].append(data['results'][i]["genre_ids"][j])
        #     file_data["fields"]["original_title"] = data['results'][i]["original_title"]
        #     file_data["fields"]["original_language"] = data['results'][i]["original_language"]
        #     file_data["fields"]["overview"] = data['results'][i]["overview"]
        #     file_data["fields"]["release_date"] = data['results'][i]["release_date"]
        #     file_data["fields"]["poster_path"] = data['results'][i]["poster_path"]
        #     file_data["fields"]["popularity"] = data['results'][i]["popularity"]
        #     file_data["fields"]["title"] = data['results'][i]["title"]
        #     file_data["fields"]["vote_count"] = data['results'][i]["vote_count"]
        #     file_data["fields"]["vote_average"] = data['results'][i]["vote_average"]
        #     output.append(file_data)
        return data


def tmdb_toprated():
    URL = f"https://api.themoviedb.org/3/movie/top_rated/?api_key={api_key}&language=ko"
    response = requests.get(URL)
    data = json.loads(response.text)
    print(1)
    return data

# tmdb_search('movie','어벤져스',1)
# print(tmdb_search('movie','어벤져스',1))

# for movie in movie_list:
#     url = f"https://api.themoviedb.org/3/movie/{movie}?api_key={api_key}&language=ko-kr"
#     response = requests.get(url)
#     file_data = OrderedDict()
#     if response.status_code == 200:
#         data = json.loads(response.text)
#         file_data["model"] = "movies.movie"
#         file_data["pk"] = data["id"]
#         file_data["fields"] = dict()
#         file_data["fields"]["adult"] = data["adult"]
#         file_data["fields"]["backdrop_path"] = data["backdrop_path"]
#         file_data["fields"]["genres"] = list()
#         for i in range(len(data["genres"])):
#             file_data["fields"]["genres"].append(data["genres"][i]["id"])
#         file_data["fields"]["original_title"] = data["original_title"]
#         file_data["fields"]["original_language"] = data["original_language"]
#         file_data["fields"]["overview"] = data["overview"]
#         file_data["fields"]["release_date"] = data["release_date"]
#         file_data["fields"]["poster_path"] = data["poster_path"]
#         file_data["fields"]["popularity"] = data["popularity"]
#         file_data["fields"]["title"] = data["title"]
#         file_data["fields"]["vote_count"] = data["vote_count"]
#         file_data["fields"]["vote_average"] = data["vote_average"]
#         output.append(file_data)
#     else:
#         continue
# with open('check.json', mode='a', encoding='utf-8') as make_file:
#     make_file.write(json.dumps(output))

