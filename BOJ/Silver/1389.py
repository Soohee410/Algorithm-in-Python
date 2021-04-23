import sys
input = sys.stdin.readline
inf = 10**4

def Solution():
    n, m = map(int, input().split())
    graph = [[inf] * (n+1) for _ in range(n+1)]
    for a in range(1, n+1):
        graph[a][a] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    #Floyd-Warshall
    for k in range(1, n+1):
        for a in range(1, n+1):
             for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    min_bacon, min_user = inf, 0
    for a in range(1, n+1):
        tmp = sum(graph[a][1:])
        if tmp < min_bacon:
            min_bacon = tmp
            min_user = a

    print(min_user)

Solution()
