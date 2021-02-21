import sys

N,K = map(int, sys.stdin.readline().split())
A = sorted(list(map(int,sys.stdin.readline().split())))
B = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)

for i in range(K):
  if A[i] >= B[i]: break
  A[i], B[i] = B[i], A[i]

print(sum(A))
