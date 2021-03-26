# First Solution

import math

def Solution(N):
    nums = list(str(math.factorial(N)))
    cnt = 0
    for i in range(len(nums)-1,-1,-1):
        if nums[i] != '0':
            return cnt
        cnt += 1
    return cnt

N = int(input())
print(Solution(N))



# ---------------------------
# More advanced Solution

N = int(input())
print(N//5 + N//25 + N//125)
