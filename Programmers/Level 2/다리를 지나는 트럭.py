from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    weights = deque([])
    times = deque([])

    truck = iter(truck_weights)
    weights.append(next(truck, False))
    times.append(0)
    cur = next(truck, False)

    while weights:
        answer += 1
        times = deque([t+1 for t in times])

        if times[0] == bridge_length:
            times.popleft()
            weights.popleft()

        if cur and len(times)+1 <= bridge_length and sum(weights)+cur <= weight:
            times.append(0)
            weights.append(cur)
            cur = next(truck, False)

    return answer


# -----------------------------------------
# Simpler solution but slower
def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length  #다리 위의 무게 리스트
    sec=0

    while q:
        sec+=1
        q.pop(0)

        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:  #다리 위의 무게 + 다음 대기 트럭이 한도를 넘지 않으면,
                q.append(truck_weights.pop(0))   #다리 위 무게 리스트에 포함.
            else:
                q.append(0)  #아닐 경우 sum에 영향을 받지 않기 위한 0 부여.

    return sec
