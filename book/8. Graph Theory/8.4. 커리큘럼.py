from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)  #진입차수 테이블
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)  #각 강의 시간

for i in range(1,v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,v+1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기.
        for i in graph[now]:
            result[i] = max(result[now] + time[i], result[i])
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)

    for i in range(1,v+1):
        print(result[i])

topology_sort()
