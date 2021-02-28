from sys import stdin
from collections import Counter

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
X = list(map(int, stdin.readline().split()))

count = Counter(A)
print(' '.join(str(count[i]) for i in X))
