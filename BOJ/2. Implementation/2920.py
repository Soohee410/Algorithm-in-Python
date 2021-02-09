A = list(map(int, input().split()))
B = A.copy()

if A[0]==1:
    A.sort()
    if B==A: print('ascending')
    else: print('mixed')

elif A[0]==8:
    A.sort(reverse=True)
    if B==A: print('descending')
    else: print('mixed')

else: print('mixed')
