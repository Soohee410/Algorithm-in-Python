# O(ElogE)
# 가장 적은 비용으로 모든 노드 연결.

def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적 호출.
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


#입력
v, e = map(int, input().split())  #노드 개수, 간선 개수

parent = [0] * (v+1)  #부모 테이블
for i in range(1, v+1):
    parent[i] = i  #초기화

edges = []  #간선 정보
for _ in range(e):
    a, b, cost = map(int, input().split()))
    edges.append((cost, a, b))

edges.sort() #비용 순으로 정렬

result = 0
for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우 최소 신장 트리에 포함.
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

#출력
print(result)
