import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
    result = {
        'genre_ids': movie.get('genre_ids'),
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }    # 주어진 딕셔너리 movie에서 필요한 키와 밸류 값들만 
         # 가지고 새로운 딕셔너리를 정의해준다.
    return result
         # 그 딕셔너리를 결과로 보여주도록 되돌린다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))