# Solution1 by DP  : 664ms
# d[i] : i번째 병사가 마지막으로 배치된 경우의 병사 수.

import sys
input = sys.stdin.readline

def Solution():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * n

    for i in range(1,n):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(n-max(dp))

Solution()


# ---------------------------------------------------
# Solution2 by LIS: 68ms
# i번째 병사가 들어갈 위치가 맨 끝이라면 수 증가, 아니면 교체만.

import sys
from bisect import bisect_left
input = sys.stdin.readline

def LIS(arr):
    best = []
    for i in arr:
        pos = bisect_left(best, i)
        if pos >= len(best):
            best.append(i)
        else:
            best[pos] = i
    return len(best)

def Solution():
    n = int(input())
    arr = reversed(list(map(int, input().split())))
    print(n - LIS(arr))

Solution()
