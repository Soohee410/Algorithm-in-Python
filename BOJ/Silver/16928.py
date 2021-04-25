import sys
from collections import deque
input = sys.stdin.readline
inf = 100

def bfs(G,visit):
    que = deque([1])
    visit[1] = 0

    while que:
        v = que.popleft()

        if visit[v] >= visit[100]:
            continue

        for step in range(1,7):
            if v + step > 100:
                continue
            num = G[v + step]

            if visit[num] >= inf:
                que.append(num)
                visit[num] = visit[v] + 1

    return visit[100]


def Solution():
    n, m = map(int, input().split())
    G = list(range(101))
    for _ in range(n+m):
        x, y = map(int, input().split())
        G[x] = y

    visit = [inf] * 101

    print(bfs(G,visit))

Solution()
