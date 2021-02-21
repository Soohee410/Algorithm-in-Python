#우선순위 큐를 이용하는 것이 효과적
import sys
import heapq
N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    heapq.heappush(heap,int(sys.stdin.readline()))

num = 0
while len(heap) > 1:
    card1, card2 = heapq.heappop(heap), heapq.heappop(heap)
    value = card1 + card2
    heapq.heappush(heap, value)
    num += value

print(num)
