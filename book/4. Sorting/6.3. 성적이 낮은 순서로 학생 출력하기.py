import sys

N = int(sys.stdin.readline())

std = []
for _ in range(N):
    name, age = sys.stdin.readline().split()
    std.append((name,int(age)))

std.sort(key = lambda x: x[1])

for i in std: print(i[0], end=' ')
