import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    H,W,N = map(int, sys.stdin.readline().split())
    y = math.ceil(N/H)
    x = H if N%H==0 else N%H
    print('%d%02d' %(x,y))
