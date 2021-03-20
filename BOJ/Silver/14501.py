import sys
read = sys.stdin.readline

n = int(read())
arr = [tuple(map(int,read().split())) for _ in range(n)]
arr.append((0,0))


d = [0] * (n+2)    #dp table
# d[i] := i번째 날까지의 최대 이익

for i in range(1, n+2):
    t, p = arr[i-1]
    d[i] = max(d[i-1], d[i])

    if i+t > n+1:
      continue

    d[i+t] = max(d[i+t-1], d[i+t], d[i]+p)

print(d[n+1])
