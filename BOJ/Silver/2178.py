from sys import stdin
from collections import deque

def bfs(graph,N,M):
  x, y = 0, 0
  dx, dy = [-1,1,0,0], [0,0,-1,1]
  que = deque([(x,y)])

  while que:
    x, y = que.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]

      if nx<0 or nx>N-1 or ny<0 or ny>M-1:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        que.append((nx,ny))

  return graph[N-1][M-1]


N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
print(bfs(graph,N,M))
