# 무방향 그래프 내에서 사이클 판별.
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

for i in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)


cycle = False

for i in range(e):
    a, b = map(int, input().split())
    #루트 노드가 같다면 사이클이 발생한 것.
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union(parent, a, b)

#출력 : 사이클 발생 여부
print('yes' if cycle else 'no')
