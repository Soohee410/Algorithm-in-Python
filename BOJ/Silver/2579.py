# Solution1

from sys import stdin

n = int(stdin.readline())
scr = [0] + [int(stdin.readline()) for _ in range(n)]

def Solution(n,scr):
  if n < 3:
    return sum(scr)
  else:
    dp = [ 0 , scr[1], scr[1]+scr[2] ] + [0] * (n-2)
    for i in range(3,n+1):
        dp[i] = max(dp[i-3]+scr[i-1]+scr[i], dp[i-2]+scr[i])
    return dp[n]

print(Solution(n,scr))



# -------------------------------------
# Solution2

from sys import stdin

n = int(stdin.readline())

a,b,c = 0,0,0

for _ in range(n):
    x = int(stdin.readline())
    t1, t2, t3 = max(b,c), a+x, b+x
    a, b, c = t1, t2, t3

print(max(t2,t3))
