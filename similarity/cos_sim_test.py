from similarity import cos_sim
from konlpy.tag import Okt
from itertools import combinations as combi

def word2one_hot(total_words:dict, tokens:list):
    res = [0] * len(total_words)
    for t in tokens:
        res[total_words[t]] += 1
    return res

okt = Okt()
data = ['안녕 나는 애플을 만든 스티브잡스야', '안녕 나는 페이스북을 만든 주커버그야',
        '나는 애플과 스티브잡스를 좋아해. 주커버그는 별로야']
tokens = []
token_set = set()

for t in data:
    token = okt.nouns(t)
    tokens.append(token)
    token_set.update(token)

total_t = {w:i for i, w in enumerate(token_set)}
vec = [word2one_hot(total_t, token) for token in tokens]

cos_sims = [cos_sim(v[0], v[1]) for v in combi(vec, 2)]

print(cos_sims)
# [0.5, 0.6708203932499369, 0.4472135954999579]