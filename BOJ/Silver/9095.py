from sys import stdin, stdout

T = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(T)]

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 12):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

stdout.write("\n".join([str(dp[j]) for j in nums]))
