N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

count = 0
for i in coins:
    if K==0: break
    else:
        count += K//i
        K = K%i

print(count)
