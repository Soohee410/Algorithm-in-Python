import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y, graph, n, col, col2):
    if x<0 or x>n-1 or y<0 or y>n-1:
        return False
    if graph[x][y] == col:
        graph[x][y] = col2   #방문한 곳은 O로 표기.
        dfs(x-1, y, graph, n, col, col2)
        dfs(x+1, y, graph, n, col, col2)
        dfs(x, y-1, graph, n, col, col2)
        dfs(x, y+1, graph, n, col, col2)
        return True
    return False


def count_dfs(graph, n, col, col2):
    result = 0
    for x in range(n):
        for y in range(n):
            if dfs(x, y, graph, n, col, col2):
                result += 1
    return result


def Solution():
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]

    #비적록색약
    ans1 = count_dfs(graph, n, 'R', 'O')   #방문한 R --> O
    ans1 += count_dfs(graph, n, 'G', 'O')  #방문한 G --> O
    cnt_B = count_dfs(graph, n, 'B', 'K')  #방문한 B --> K
    ans1 += cnt_B

    #적록색약
    ans2 = cnt_B
    ans2 += count_dfs(graph, n, 'O', 'K')  #방문한 O --> K

    print(ans1, ans2)

Solution()
