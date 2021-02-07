#처음 결과나 새로 연산할 숫자가 0또는 1이면 더하고, 아니면 곱한다.

num = str(input())
n = len(num)

nums = []
for i in range(n):
    nums.append(int(num[i]))

result = 0

for i in nums:
    if i<=1 or result<=1:
        result += i
    else:
        result *= i

print(result)
