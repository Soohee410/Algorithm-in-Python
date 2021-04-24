# R이라고 매번 reverse하면 시간 초과.
# D일 때도 그 때마다 제거 안하고 풀 수 있음.
# input바꿀 때 parsing 주의하기.
# 빈 리스트인 줄 알았는데 ''이 들어가 있어서 오류 뜸.

import sys
from collections import deque
input = sys.stdin.readline

def AC(p,arr):
    R_idx = 0
    for i in p:
        if i == 'R':
            R_idx = (R_idx + 1) % 2
        else:
            if arr and not R_idx: arr.popleft()
            elif arr and R_idx: arr.pop()
            elif not arr: return 'error'
    if not R_idx:
        return '[' + ','.join(arr) + ']'
    else:
        return '[' + ','.join(reversed(arr)) + ']'


def Solution():
    T = int(input())
    for _ in range(T):
        p = list(input().rstrip())
        n = int(input())
        arr = deque(input().rstrip()[1:-1].split(','))
        if n == 0: arr = deque([])
        print(AC(p,arr))

Solution()
