from collections import Counter

def solution(N, stages):
    answer = []
    count = Counter(stages)
    n_player = len(stages)

    n_left = n_player
    for stage in range(1,N+1):

        if n_left==0: failure = 0
        else: failure = count[stage]/n_left

        answer.append((stage, failure))
        n_left -= count[stage]

    answer.sort(key=lambda x: x[1], reverse=True)
    answer = [stage for stage,failure in answer]

    return answer
