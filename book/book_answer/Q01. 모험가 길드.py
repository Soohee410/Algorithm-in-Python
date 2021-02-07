N = int(input())
nums = list(map(int, input().split()))

nums.sort()

group = 0
count = 0 #현재 그룹의 인원 수

for i in nums:
    count += 1
    if count >= i: #현재 그룹의 인원 수가 현재의 공포도 이상이면 그룹 결성
        group += 1
        count = 0

print(group)
