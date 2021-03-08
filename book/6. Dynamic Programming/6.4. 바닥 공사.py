N = int(input())

d = [0] * N   #DP table
d[0], d[1] = 1, 3

#bottom-up
for i in range(2,N):
    d[i] = (d[i-1] + d[i-2]*2) % 796796

print(d[N-1])
