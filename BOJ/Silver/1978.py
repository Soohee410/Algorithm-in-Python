#sqrt(n)까지만 확인해도 소수 판별 가능.
def is_prime(x):
    for i in range(2, round(x**(1/2))+1):
        if x%i == 0: return False
    return True

import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
count = 0
for num in nums:
    if num ==1: continue
    elif num==2: count += 1
    else:
        if is_prime(num): count += 1
            
print(count)
