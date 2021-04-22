import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(c):
    q = []
    heapq.heappush(q, (0,c))
    distance[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt, max_distance = 0, 0
for d in distance:
    if d != inf:
        cnt += 1   #갈 수 있는 도시 카운트.
        max_distance = max(max_distance, d)  #최대 시간이 총 소요 시간.

print(cnt-1, max_distance)
