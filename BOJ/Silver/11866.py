import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
que = list(range(1,N+1))

print('<', end='')
while len(que)>1 :
  for _ in range(K-1):
    tmp = que.pop(0) 
    que.append(tmp)
  print(que.pop(0), end=', ')

print('%d>' %que[0])



#-------------------------------------------
# Simpler and Faster code

N, K = map(int, input().split())
l = list(range(1, N+1))
p = list()
i = 0
while l:
    i = (i+K-1) % len(l)
    p.append(str(l.pop(i)))

print('<'+', '.join(p)+'>')
