from sys import stdin
inf = int(1e9)

n, m = int(input()), int(input())
graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == inf:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
