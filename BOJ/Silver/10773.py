import sys

K = int(sys.stdin.readline())
stk = []

for _ in range(K):
  value = int(sys.stdin.readline())
  if value != 0: stk.append(value)
  else: stk.pop()

print(sum(stk))
