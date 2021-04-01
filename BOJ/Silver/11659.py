import sys
read = sys.stdin.readline

N, M = map(int, read().split())
nums = [0] + list(map(int, read().split()))
for k in range(1,N+1):
    nums[k] = nums[k-1] + nums[k]

for _ in range(M):
    i, j = map(int, read().split())
    print(nums[j]-nums[i-1])
