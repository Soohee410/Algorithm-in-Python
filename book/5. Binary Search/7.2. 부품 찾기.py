# Solution1 : 이진 탐색
from sys import stdin

def binary_search(array,target,start,end):
  if start > end:
    return False
  mid = (start+end)//2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

N = int(stdin.readline())
store = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
ctmr = list(map(int, stdin.readline().split()))


for i in ctmr:
  if binary_search(store,i,0,N-1) : print('yes', end=' ')
  else: print('no', end=' ')


# -------------------------------------------------------------------
# Solution2 : 계수 정렬
from sys import stdin

N = int(stdin.readline())
store = [0]*1000000
for i in stdin.readline().split():
    store[int(i)] = 1

M = int(stdin.readline())
ctmr = list(map(int, stdin.readline().split()))

for j in ctmr:
  if store[j] == 1: print('yes', end=' ')
  else: print('no', end=' ')



# -------------------------------------------------------------------
# Solution3 : set() 이용해서 들어있는지 아닌지 단순 확인
from sys import stdin

N = int(stdin.readline())
store = set(map(int, stdin.readline().split()))

M = int(stdin.readline())
ctmr = list(map(int, stdin.readline().split()))

for j in ctmr:
  if j in store: print('yes', end=' ')
  else: print('no', end=' ')
