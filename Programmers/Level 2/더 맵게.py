#First Solution
import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for x in scoville:
        heapq.heappush(h, x)

    while h:
        a = heapq.heappop(h)
        if not h:
            if a >= K:
                return answer
            else:
                return -1

        b = heapq.heappop(h)
        if a >= K and b >= K:
            return answer

        new = a + (b *2)
        heapq.heappush(h, new)
        answer += 1

    return -1


# -------------------------------------------------
# clean version
import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while True:
        a = hq.heappop(scoville)
        if a >= K:
            break
        if not scoville:
            return -1

        b = hq.heappop(scoville)

        hq.heappush(scoville, a + b *2)
        answer += 1

    return answer
