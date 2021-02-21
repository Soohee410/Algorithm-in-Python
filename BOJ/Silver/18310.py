import sys

N = int(sys.stdin.readline())
home = sorted(list(map(int, sys.stdin.readline().split())))
print(home[(N-1)//2])
