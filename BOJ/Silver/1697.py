#First Solution - BFS : 532ms
from sys import stdin
from collections import deque

def SolbyBFS(n,k,arr):
    arr[n] = 0
    que = deque([n])
    while que:
        x = que.popleft()
        if x >= k :
            arr[k] = min(arr[x] + (x-k), arr[k])
        else:
            for nx in [x*2, x+1, x-1]:
                if nx >= 0 and nx < 100001 and arr[nx] >= arr[x]+1:
                    arr[nx] = arr[x] + 1
                    que.append(nx)
    return arr[k]


n, k = map(int, stdin.readline().split())
arr = [1e9] * 100001
print(SolbyBFS(n,k,arr))



#------------------------------------
#More advanced solution - BFS : 124ms
def solbyBfs(n,k):
    visit = [False] * 100001
    que = [n]
    cnt = 0

    if n>k : return n-k

    while que:
        stage = []   #cnt=t+1번째 시도에서의 수빈이의 자리들
        for x in que:
            if x == k:
                return cnt
            else:
                for nx in [x-1, x+1, x*2]:
                    if nx>=0 and nx<=k+1 and not visit[nx]:
                        visit[nx] = True
                        stage.append(nx)
        que = stage
        cnt += 1

n, k = map(int, input().split())
print(SolbyBfs(n,k))



#------------------------------------
#Another solution - 재귀 : 80ms
def Sol(n,k):
    if n >= k :
        return n-k
    elif k == 1:
        return 1
    elif k % 2:   #2로 나누어 떨어지지 않으면,
        return min(Sol(n,k-1), Sol(n,k+1)) + 1
    else:        #2로 나누어 떨어지면,
        return min(k-n, Sol(n,k//2)+1)

n, k = map(int, input().split())
print(Sol(n,k))
