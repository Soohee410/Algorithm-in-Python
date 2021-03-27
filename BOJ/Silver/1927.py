from sys import stdin
import heapq

def MinHeap(h,x):
    if x:
        heapq.heappush(h,x)
    else:
        print(0 if not h else heapq.heappop(h))


N = int(stdin.readline())
h = []

for _ in range(N):
    x = int(stdin.readline())
    MinHeap(h,x)
