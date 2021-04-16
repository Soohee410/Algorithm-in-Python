from sys import stdin, stdout
from collections import deque

n = int(stdin.readline())
G = [list(stdin.readline().rstrip()) for _ in range(n)]

def SolbyBFS():
    que1 = deque([])
    for row in range(n):
        for col in range(n):
            if G[row][col] == '1':
                que1.append((row,col))

    dx, dy = [-1,1,0,0], [0,0,-1,1]
    cnt1, homes = 0, []  #단지수, 단지 내 집 수 담을 리스트

    while que1:
        startx, starty = que1.popleft()  #starting point
        if G[startx][starty]=='0':
            continue  #이미 방문해서 0으로 처리되었으면 넘어감.

        que2 = deque([(startx,starty)])
        G[startx][starty] = '0'
        cnt1 += 1    #단지 수 1 증가.
        cnt2 = 1     #단지 내 집 수 1로 초기화.

        while que2:   #단지 내 집 수 찾는 과정.
            x, y = que2.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or nx>n-1 or ny<0 or ny>n-1:
                    continue

                if G[nx][ny] == '1':
                    G[nx][ny] = '0'
                    cnt2 += 1
                    que2.append((nx,ny))

        homes.append(cnt2)

    return [cnt1] + sorted(homes)


result = SolbyBFS()
stdout.write('\n'.join([str(j) for j in result]))
