import sys
N = int(input())
nums = list(int(sys.stdin.readline()) for _ in range(N))
nums.sort()
for i in nums: print(i)

#-------------------------------
#more fast one
import sys
N = int(sys.stdin.readline())
nums = sorted(list(map(int,sys.stdin.read().split())))
print('\n'.join(map(str,nums)))
