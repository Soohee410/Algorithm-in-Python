from sys import stdin
import heapq

def AbsMinHeap(h,x):
    if x>0:
        heapq.heappush(h,(x,x))
    elif x<0:
        heapq.heappush(h,(-x,x))
    else:
        print(0 if not h else heapq.heappop(h)[1])

N = int(stdin.readline())
h = []
for _ in range(N):
    x = int(stdin.readline())
    AbsMinHeap(h,x)
