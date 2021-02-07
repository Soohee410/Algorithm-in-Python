#0인 그룹과 1인 그룹 개수를 구해서, 둘 중 작은 것의 개수 출력.

num = input()
nums = []
for i in range(len(num)):
    nums.append(int(num[i]))

group0, group1 = 0,0

before = nums[0]
if before==0:
    group0 += 1
else:
    group1 += 1

for i in range(1,len(nums)):
    if nums[i] != before:
        if nums[i]==0:
            group0 += 1
        else:
            group1 += 1
    before = nums[i]

print(min(group0,group1))
