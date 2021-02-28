# Solution1: Binary Search
def Search_bee(N):
  start, end = 1, 19000

  while start<= end:
    mid = (start+end)//2
    lb = 3*(mid**2)-3*mid+1
    ub = lb + 6*mid

    if N > lb and N <= ub:
      return mid+1
    elif N == lb :
      return mid
    elif N < lb:
      end = mid
    else:
      start = mid


N = int(input())
print(Search_bee(N))


# -------------------------------------------------------
# Solution2: 근의 공식
N = int(input())
print(int(-(-(3+(12*N-3)**.5)//6)))
