N,M = map(int, input().split())

result = 0
for i in range(N):
    row = list(map(int, input().split()))
    result = max(min(row), result)

print(result)
