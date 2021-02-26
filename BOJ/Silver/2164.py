from collections import deque

N = int(input())
que = deque(range(1,N+1))

while len(que)>1:
    que.popleft()
    tmp = que.popleft(); que.append(tmp)
    
print(que[0])
