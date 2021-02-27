from sys import stdin

s1 = 'WB'*4; s2 = 'BW'*4
V1 = ''.join(([s1]+[s2])*4)
V2 = ''.join(([s2]+[s1])*4)

def Chess(N,M,data):
  minimum = float('inf')

  for row in range(N-8+1):
    for col in range(M-8+1):
      count1 = 0; count2 = 0
      tmp = ''.join(frac[col:8+col] for frac in data[row:row+8])

      for i,j,k in zip(tmp,V1,V2):
        if i!=j: count1+=1
        if i!=k: count2+=1

      minimum = min(minimum,count1,count2)

  return minimum


N,M = map(int, stdin.readline().split())
data = [stdin.readline().rstrip() for _ in range(N)]
print(Chess(N,M,data))
