# Solution1: BFS
import sys
from collections import deque

def bfs(graph, v, visit):
	que = deque([v])
	visit[v] = True
	while que:
		v = que.popleft()
		for i in graph[v]:
			if not visit[i]:
				que.append(i)
				visit[i] = True

read = sys.stdin.readline
N, M = map(int, read().split())

graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    v1,v2 = map(int, read().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visit = [False] * (N+1)
cnt = 0

for v in range(1, N+1):
    if visit[v]: continue
    bfs(graph, v, visit)
    cnt += 1

print(cnt)


# -------------------------------------
# Solution2: dfs
import sys
sys.setrecursionlimit(10000)  # 재귀 제한을 확대해야 함.

def dfs(graph, v, visit):
	visit[v] = True
	for i in graph[v]:
		if not visit[i]:
			dfs(graph, v, visit)

read = sys.stdin.readline
N, M = map(int, read().split())

graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    v1,v2 = map(int, read().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visit = [False] * (N+1)
cnt = 0

for v in range(1, N+1):
    if visit[v]: continue
    dfs(graph, v, visit)
    cnt += 1

print(cnt)
