import sys
from collections import deque

N,M,V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = True
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

visit_dfs = [False]*(N+1)
visit_bfs = [False]*(N+1)

dfs(graph, V, visit_dfs); print()
bfs(graph, V, visit_bfs)
