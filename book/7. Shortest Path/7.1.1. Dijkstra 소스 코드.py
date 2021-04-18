#우선순위 큐 이용: O(ElogV)
import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

# 입력 받기 및 초기화
n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input())  #시작 위치

distance = [inf] * (n+1)  #최단 거리 테이블 무한으로 초기화.
graph = [[] for _ in range(n+1)] #그래프 정보 담는 리스트 생성.

for _ in range(m):
    a, b, c = map(int, input().split())  #a 노드에서 b 노드로 가는 비용이 c.
    graph[a].append((b,c))


# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        #이미 처리된 노드이면 무시.
        if distance[now] < dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드들에 대하여,
        #현재 노드를 거쳐갔을 때의 거리가, 더 짧은 경우 거리 정보 갱신하고, 우선순위큐에 담는다.
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))


#알고리즘 수행.
dijkstra(start)

#시작 노드에서 모든 노드까지의 최단 거리 출력.
for i in range(1, n+1):
    if distance[i] == inf:
        print('Infinity')
    else:
        print(distance[i])
