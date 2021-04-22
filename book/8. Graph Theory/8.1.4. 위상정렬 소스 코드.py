from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)  #진입차수 테이블
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1,v+1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기.
        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()
