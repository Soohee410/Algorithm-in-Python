import sys
N = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
for i in nums:
    sys.stdout.write(str(i)+'\n')
