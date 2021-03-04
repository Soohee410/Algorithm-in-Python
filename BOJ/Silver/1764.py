# First Solution: 58476KB / 200ms / 674B
def BS(array,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid][1] == 1 and array[mid-1][1]==2: return mid
        elif array[mid][1] == 2: start = mid+1
        else: end = mid-1
    return None

def Solution(data):
    data = sorted(data.items(), key=lambda x:(-x[1],x[0]))
    midpoint = BS(data,0,N+M-1)
    if midpoint == None:
      print(0)
    else:
      print(midpoint)
      stdout.write('\n'.join(map(str,dict(data[:midpoint]).keys())))


from sys import stdin,stdout
from collections import Counter

N, M = map(int, stdin.readline().split())
data = Counter([stdin.readline().rstrip() for _ in range(N+M)])
Solution(data)


# ---------------------------------------------------------
# More Advanced Solution: 41884KB / 124ms / 272B

from sys import stdin,stdout

N, M = map(int, stdin.readline().split())
hear = set([stdin.readline().rstrip() for _ in range(N)])
see = set([stdin.readline().rstrip() for _ in range(M)])

common = sorted(list(hear & see))
print(len(common))
stdout.write('\n'.join(common))
