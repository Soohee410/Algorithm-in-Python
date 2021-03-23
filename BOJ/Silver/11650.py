import sys

N = int(input())
coord = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(N)])

for x,y in coord:
    print(x,y)
