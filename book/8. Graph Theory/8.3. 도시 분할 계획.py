#연결된 전체 간선 중 가장 비용 큰 간선 하나 빼기.
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def Solution():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c,a,b))
    edges.sort()

    result, max_c = 0, 0
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            result += cost
            max_c = cost

    print(result-max_c)

Solution()
