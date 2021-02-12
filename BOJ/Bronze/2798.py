import sys
N, M = map(int, input().split())
cards = list(map(int, sys.stdin.readline().split()))

import itertools
result = 0
for x in itertools.combinations(cards, 3):
    if sum(x)<=M and sum(x)>result: result = sum(x)

print(result)
