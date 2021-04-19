#Solution1 - 플로이드 워셜. (264ms)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] or (graph[a][k] + graph[k][b]) > 1:
                graph[a][b] = 1

for a in range(n):
    for b in range(n):
        print(graph[a][b], end=' ')
    print()



#Solution2 - DFS 이용. (84ms)
n = int(input())
edge = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            edge[i].append(j)

def dfs(start, visit):
    for x in edge[start]:
        if not visit[x]:
            visit[x] = 1
            dfs(x, visit)

for x in range(n):
    visit = [0] * n
    dfs(x, visit)
    print(' '.join(map(str,visit)))
