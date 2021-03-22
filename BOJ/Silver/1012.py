import sys
sys.setrecursionlimit(10000)

read = sys.stdin.readline

def dfs(x,y,graph,M,N):
    if x<0 or x>M-1 or y<0 or y>N-1:
        return False

    if graph[y][x] == 1:          # 아직 방문하지 않은 배추 심은 곳일 경우,
        graph[y][x] = 0           # 방문 표시로 0으로 바꿈.
        dfs(x-1, y, graph, M, N)
        dfs(x, y-1, graph, M, N)
        dfs(x+1, y, graph, M, N)
        dfs(x, y+1, graph, M, N)
        return True              # 연결된 모든 지점 방문 후 True 반환.

    return False


def Solution():
    M, N, K = map(int, read().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, read().split())
        graph[y][x] = 1

    result = 0
    for y in range(N):
        for x in range(M):
            if dfs(x, y, graph, M, N):   # True일 경우 카운팅.
                result += 1
    print(result)


T = int(read())

for _ in range(T):
    Solution()
