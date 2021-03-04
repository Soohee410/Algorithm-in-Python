# Solution1-bfs: 32704KB / 92ms
from sys import stdin
from collections import deque

def bfs(graph, start, N):
    visited, cnt = [False]*(N+1), 0
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        for i in graph[v]:
          if not visited[i]:
            que.append(i)
            visited[i] = True
            cnt += 1
    return cnt

N,M = int(stdin.readline()), int(stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(graph,1,N))
