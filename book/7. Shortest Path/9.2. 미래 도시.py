#노드 개수가 100 이하로 한정적이므로, 구현이 더 간단한 플로이드 워셜 알고리즘 사용하면 됨.
#최소 이동 시간 = (1번 노드에서 k번 노드까지 최소 이동 시간) + (k번 노드에서 x번 노드까지 최소 이동 시간)

inf = int(1e9)

n, m = map(int, input().split())
graph = [[inf] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= inf:
    print('-1')
else:
    print(distance)
