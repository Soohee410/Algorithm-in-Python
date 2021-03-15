nums = []
for i in range(1,46):
    nums += [i] * i

a,b = map(int, input().split())
print(sum(nums[a-1:b]))
