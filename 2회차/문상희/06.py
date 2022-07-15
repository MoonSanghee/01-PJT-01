import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    movie_col = []
    # 영화 정보들을 저장해줄 리스트를 생성한다.
    for movie in movies:
        # movies라는 폴더속 딕셔너리를 차례로 훑어준다.
        genre_ids = movie['genre_ids']
        names = []
        for genre in genres:
            if genre['id'] in genre_ids:
                names.append(genre['name'])
                # 05.py에서 name 값을 새로 만들어준 과정과 동일

        movie_info = {
            'genre_names' : names,        
            'id': movie.get('id'),
            'title' : movie.get('title'),
            'vote_average' : movie.get('vote_average'),
            'overview' : movie.get('overview')
        }
        movie_col.append(movie_info)
        # 영화 정보가 들어간 딕셔너리를 movie_col이라는 리스트에 추가한다.
    return movie_col
    # 함수의 결과로  movie_info들이 저장된 movie_col을 돌려준다.
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))