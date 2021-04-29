#Solution1
from collections import Counter

def solution(participant, completion):
    data = Counter(participant)

    for i in completion:
        data[i] -= 1

    return sorted(data.items(), key=lambda x: x[1])[-1][0]



# -----------------------------------------------------------------
# More simple Solution
import collections

def solution(participant, completion):
    #딕셔너리끼리 빼면 됨!!!
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]


# Another solution:
# participant, completion 모두 정렬 후 하나씩 비교해보면 됨.
