# Solution1: 147856KB / 3030ms

def BS_tree(data,M):
    start,end = 0, max(data)
    result = 0
    while start<= end:
        total = 0
        mid = (start+end)//2
        for x in data:
          if x > mid:
            total += x-mid

        if total < M:
            end = mid -1
        else:
            result = mid
            start = mid + 1

    return result

from sys import stdin
N,M = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))
print(BS_tree(data,M))



# ---------------------------------------------------------
# Solution2: 114920KB, 456ms 
# Counter 이용

def BS_tree(data,M):
    start, end = 0, max(data)
    result = 0
    while start<= end:
        total = 0
        mid = (start+end)//2
        for x,num in data.items():
          if x > mid:
            total += (x-mid)*num

        if total < M:
            end = mid -1
        else:
            result = mid
            start = mid + 1

    return result

from sys import stdin
from collections import Counter
_, M = map(int, stdin.readline().split())
data = Counter(map(int, stdin.readline().split()))
print(BS_tree(data,M))
