def Division_sum(N):
    length = len(str(N))

    for i in range(max(1,N-9*length), N+1):
        tmp = i + sum([int(j) for j in str(i)])
        if tmp == N: return i

    if i == N: return 0


N = int(input())
print(Division_sum(N))
