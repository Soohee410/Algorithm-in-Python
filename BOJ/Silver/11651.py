import sys
N = int(input())
coord = []
for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    coord.append([y,x])
for y,x in sorted(coord): print(x,y)
