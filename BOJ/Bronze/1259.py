nums = []
while True:
    num = input()
    if num == '0': break
    nums.append(num)

for i in nums:
    if i == i[::-1]: print('yes')
    else: print('no')
