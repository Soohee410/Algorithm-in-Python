#그냥 input쓰면 시간초과됨
from collections import Counter #mode
import sys

N = int(input())
data = [int(sys.stdin.readline()) for _ in range(N)]
print("%.0f" %(sum(data)/N)) #mean

data.sort()
print(data[N//2]) #mid

A = Counter(data)
B = A.most_common(); maximum = B[0][1]
mode_list = [x for x,y in B if y==maximum]
mode_list.sort()
print(mode_list[0]) if len(mode_list)==1 else print(mode_list[1])

print(data[N-1]-data[0]) #range
