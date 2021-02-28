# Solution1: 44700KB / 712ms
def binary_search(array,target,start,end):
  if start>end: return None
  mid = (start+end)//2
  if array[mid] == target:
    return mid
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

from sys import stdin
N = int(stdin.readline())
A = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline())
X = list(map(int, stdin.readline().split()))

for i in X:
  if binary_search(A,i,0,N-1)!=None: print(1)
  else: print(0)


# -----------------------------------------------------
# Solution2 : 47988KB / 164ms

from sys import stdin
N = int(stdin.readline())
A = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
X = list(map(int, stdin.readline().split()))

print('\n'.join('1' if i in A else '0' for i in X ))
