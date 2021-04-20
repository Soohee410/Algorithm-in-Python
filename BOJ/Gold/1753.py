import sys
import heapq

input = sys.stdin.readline
inf = int(1e9)

def dijkstra(G,s,distance):
    q = []
    heapq.heappush(q, (0,s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in G[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def Solution():
    v, e = map(int, input().split())
    s = int(input())
    G = [[] for _ in range(v+1)]
    distance = [inf] * (v+1)

    for _ in range(e):
        u, v, w = map(int, input().split())
        G[u].append((v,w))

    dijkstra(G, s, distance)

    for result in distance[1:]:
        if result == inf:
            print('INF')
        else:
            print(result)

Solution()
