# 에라토스테네스의 체 이용
M, N = map(int, input().split())

nums = [True for i in range(N+1)]
nums[1] = False

for i in range(2, int(N**(1/2))+1):
    if nums[i] == True:
        j = 2
        while i*j <= N:
            nums[i*j] = False
            j += 1

for i in range(M, N+1):
    if nums[i] == True: print(i)
