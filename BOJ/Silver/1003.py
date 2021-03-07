from sys import stdin

def fibo(x):
      if x == 0 : return [1,0]
      elif x == 1: return [0,1]

      if d[x] != 0: return d[x]

      d[x] = [a+b for a,b in zip(fibo(x-1), fibo(x-2))]
      return d[x]


T = int(stdin.readline())

d = [0]*41
for _ in range(T):
    result = fibo(int(stdin.readline()))
    print(result[0],result[1])
