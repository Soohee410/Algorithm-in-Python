#O(N^3)
inf = int(1e9)

# 입력 받기 및 초기화
n = int(input())
m = int(input())

graph = [[inf] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    graph[a][a] = 0  #자기 자신에서 자신으로 가는 비용은 0으로 초기화.
for _ in range(m):
    a, b, c = map(int, input().split())  #a노드에서 b노드로 가는 비용이 c.
    graph[a][b] = c


#플로이드 워셜 알고리즘.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


#수행 결과 출력.
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == inf:
            print('Infinity', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
