# First solution
import sys
input = sys.stdin.readline

def TwoPointer(n, m, A):
    s, e, cnt = 0, 0, 0
    value = sum(A[s:e+1])

    while True:
        if value < m :
            if e == n-1:
                return cnt
            e += 1
            value += A[e]

        elif value > m:
            if s+1 > e:
                if e == n-1:
                    return cnt
                e += 1
                value += A[e]
            else:
                s += 1
                value -= A[s-1]

        else:
            cnt += 1
            if e == n-1:
                return cnt
            e += 1
            value += A[e]

    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    print(TwoPointer(n,m,A))


# -------------------------------------------------------
# Simpler solution
def TwoPointer(m, A):
    s, val, cnt = 0, 0, 0

    for i in A:
        val += i

        while val > m:
            val -= A[s]
            s += 1

        cnt += (val == m)

    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    print(TwoPointer(n,m,A))
