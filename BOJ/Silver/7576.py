# First Solution
from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
G = [list(map(int, stdin.readline().split())) for _ in range(n)]
que = deque([(row,col,0) for col in range(m) for row in range(n) if G[row][col]==1])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(que):
    day = 0
    while que:
        x, y, d = que.popleft()

        if d > day: day += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny<0 or ny > m-1:
                continue

            if G[nx][ny] == 0:
                G[nx][ny] = 1
                que.append((nx,ny,day+1))

    for row in range(n):
        for col in range(m):
            if not G[row][col]:
                return -1

    return day

print(bfs(que))


# -----------------------------------------------------------
# Second Solution
from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
G = [list(stdin.readline().split()) for _ in range(n)]

def SolbyBFS(G):
    que, num_0 = deque([]), 0
    for row in range(n):
        for col in range(m):
            if G[row][col] == '0':
                num_0 += 1
            elif G[row][col] == '1':
                que.append((row, col))

    day = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while que and num_0:
        l = len(que)

        for _ in range(l):
            x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > n-1 or ny<0 or ny > m-1:
                    continue

                if G[nx][ny] == '0':
                    G[nx][ny] = '1'
                    que.append((nx,ny))
                    num_0 -= 1
        day += 1

    if num_0: print(-1)
    else: print(day)

SolbyBFS(G)
