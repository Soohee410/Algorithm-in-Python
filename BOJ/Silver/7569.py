from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
G = [[list(stdin.readline().split()) for _ in range(n)] for __ in range(h)]

def SolbyBFS(G):
    que, num_0 = deque([]), 0

    for hgt in range(h):
        for row in range(n):
            for col in range(m):
                if G[hgt][row][col] == '0':
                    num_0 += 1
                elif G[hgt][row][col] == '1':
                    que.append((hgt, row, col))
    day = 0
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while que and num_0:
        l = len(que)

        for _ in range(l):
            z, x, y = que.popleft()

            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or nx>n-1 or ny<0 or ny>m-1 or nz<0 or nz>h-1:
                    continue

                if G[nz][nx][ny] == '0':
                    G[nz][nx][ny] = '1'
                    que.append((nz,nx,ny))
                    num_0 -= 1
        day += 1

    if num_0: print(-1)
    else: print(day)

SolbyBFS(G)
