def dfs(x,y):
    if x<0 or x>N-1 or y<0 or y>M-1:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False


N, M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)
