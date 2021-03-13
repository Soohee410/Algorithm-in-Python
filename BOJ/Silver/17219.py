from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

data = dict()
for _ in range(N):
  k, v = stdin.readline().split()
  data[k] = v

result = [data[stdin.readline().rstrip()] for _ in range(M)]

stdout.write("\n".join(result))
