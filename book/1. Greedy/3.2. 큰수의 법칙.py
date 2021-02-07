N,M,K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
first = nums[N-1]
second = nums[N-2]

result = 0
result += (first*K+second) * (M//(K+1))
result += first * (M%(K+1))

print(result)
