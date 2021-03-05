from sys import stdin,stdout
from collections import deque

def bfs(graph,N,X,K):
    que = deque([X])
    visited = [-1]*(N+1)
    visited[X] = 0
    while que:
        v = que.popleft()
        for i in graph[v]:
          if visited[i]==-1:
            que.append(i)
            visited[i] = visited[v]+1

    visited = [idx for idx in range(1,N+1) if visited[idx]==K]
    if len(visited)==0: return False
    return sorted(visited)


N,M,K,X = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,stdin.readline().split())
    graph[x].append(y)

result = bfs(graph,N,X,K)
if not result: print(-1)
else: stdout.write('\n'.join(str(j) for j in result))
