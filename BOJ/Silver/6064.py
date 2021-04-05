# First Solution: 2120ms

from sys import stdin
from math import gcd

def Solution(m,n,x,y):
    GCD = gcd(m,n)
    LCM = m * n / GCD
    total = x
    b = n if not x % n else x % n

    while total <= LCM :
        if b == y:
            return total
        total += m
        b = n if not (b+m)%n else (b+m)%n

    return False

T = int(stdin.readline())

for _ in range(T):
    m,n,x,y = map(int, stdin.readline().split())
    ans = Solution(m,n,x,y)
    print(-1 if not ans else ans)
