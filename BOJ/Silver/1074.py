# 재귀에 얽매여 오랫동안 잘 못 푼 문제ㅠ
# First solution
n, r, c = map(int, input().split())

def Find4(r, c):
    if 0 <= r < 2**(n-1) and 0 <= c < 2**(n-1):
        return 1
    elif 0 <= r < 2**(n-1) and 2 ** (n-1) <= c < 2**(n):
        return 2
    elif 2**(n-1) <= r < 2**(n) and 0 <= c < 2**(n-1):
        return 3
    else:
        return 4

def ChangeCoord():
    global r, c, n
    if res == 2:
        c -= 2**(n-1)
    elif res == 3:
        r -= 2**(n-1)
    elif res == 4:
        r -= 2**(n-1)
        c -= 2**(n-1)
    n -= 1

ans = 0
while True:
    if n <= 0:
        break
    res = Find4(r, c)
    ans = ans + (res-1) * (4**(n-1))
    ChangeCoord()

print(ans)


# -------------------------------------------------------
# Simpler and more advanced solution
def Z(n, x, y):
    if n == 0:
        return 0
    d = pow(2, n-1)
    s = d * d * ((x//d) * 2 + y//d)
    return s + Z(n-1, x%d, y%d)

n, x, y = map(int, input().split())
print(Z(n, x, y))
