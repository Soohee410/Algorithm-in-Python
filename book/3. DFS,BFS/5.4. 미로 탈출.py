from collections import deque

N,M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

def bfs(x,y):
    que = deque()
    que.append((x,y))

    dx, dy = [-1,1,0,0], [0,0,1,-1]

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>N-1 or ny<0 or ny>M-1:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))

    return graph[N-1][M-1]

print(bfs(0,0))
