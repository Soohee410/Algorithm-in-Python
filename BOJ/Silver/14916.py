# Solution1 : DP를 이용한 풀이.
n = int(input())

inf = float('Inf')
dp = [0] + [inf] * n

for i in range(2, min(n+1, 5)):
    dp[i] = min(dp[i], dp[i-2]+1)
    
for j in range(5,n+1):
    dp[j] = min(dp[j], dp[j-2]+1, dp[j-5]+1)

print(dp[n] if dp[n] != inf else -1)


# Solution2 : DP를 이용하지 않는 풀이. (이 문제에서는 메모리도, 시간도 더 단축)
n = int(input())
result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        n = 0
    else:
        result += 1
        n -= 2

if n < 0:
    result = -1

print(result)
