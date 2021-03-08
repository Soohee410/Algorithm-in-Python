N = int(input())
food = list(map(int,input().split()))

d = [0] * N   #DP table
d[0] = food[0]
d[1] = max(food[0], food[1])

#bottom-up
for i in range(2,N):
    d[i] = max(d[i-1], d[i-2] + food[i])

print(d[N-1])
