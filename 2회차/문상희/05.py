import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.
    genre_ids = movie['genre_ids']
    # movie라는 딕셔너리에서 genre_ids만 뽑아내서 리스트로 만든다. 
    names = []
    # id값을 names으로 변경하여 저장해줄 빈 리스트를 만든다.
    for genre in genres:
        # genres라는 딕셔너리가 모여 만들어진 리스트를
        # 딕셔너리별로 훓는다.
        if genre['id'] in genre_ids:
            # genres 속 딕셔너리들을 키 값을 제시해주며 차례로 훓는다.
            names.append(genre['name'])\
            # 비어있던 names라는 리스트에 id값을 통해 알아낸 name들을 저장해준다.

    movie_info = {
        'genre_names' : names,        
        'id': movie.get('id'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview')
    }   # 위의 for, if문을 통해 나온 name을 id대신 나오도록 딕셔너리를 설정한다.
        # 04번 문제의 ids 자리를 names로 대체
    return movie_info
        # 함수가 위의 딕셔너리값을 받도록 되돌린다.

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
    movieq_genres = movie.get('genre_ids')