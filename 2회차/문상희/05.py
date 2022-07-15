import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.
    genre_ids = movie['genre_ids']
    names = []
    for genre in genres:
        if genre['id'] in genre_ids:
            names.append(genre['name'])

    movie_info = {
        'genre_names' : names,        
        'id': movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview')
    }
    return movie_info

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
    movieq_genres = movie.get('genre_ids')