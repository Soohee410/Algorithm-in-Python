from sys import stdin

def ED(A,B):
  return (A[0]-B[0])**2 + (A[1]-B[1])**2

def isSquare(crd):
  crd.sort(key=lambda x: (x[0],x[1]))
  if ED(crd[0],crd[3]) != ED(crd[1],crd[2]):
    return 0
  else:
    if ED(crd[0],crd[1]) == ED(crd[0],crd[2]):
      return 1
    else:
      return 0


T = int (stdin.readline())

for _ in range(T):
  crd = []
  for __ in range(4):
    crd.append(tuple(map(int, stdin.readline().split())))

  print(isSquare(crd))
