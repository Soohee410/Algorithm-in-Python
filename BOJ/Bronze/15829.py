import sys

L = int(sys.stdin.readline())
word = list(sys.stdin.readline().rstrip())
r,M = 31,1234567891

H = 0
for i in range(L):
  value = ord(word[i]) - 96
  H += value*(r**i)

print(H%M)
