import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []

def CountPaper(x, y, n):
    color = arr[x][y]
    for row in range(x, x+n):
        for col in range(y, y+n):
            if color != arr[row][col]:
                CountPaper(x, y, n//2)
                CountPaper(x, y+n//2, n//2)
                CountPaper(x+n//2, y, n//2)
                CountPaper(x+n//2, y+n//2, n//2)
                return
    if not color:
        result.append(0)
    else:
        result.append(1)

CountPaper(0,0,n)
print(result.count('0'), result.count('1'), sep='\n')



# ----------------------------------------------------------------
# Another Solution
def ColorPaper(n, cp, x, y):
    if n == 1:
        return cp[x][y]   #string

    cp1 = ColorPaper(n // 2, cp, x, y)
    cp2 = ColorPaper(n // 2, cp, x, y + n // 2)
    cp3 = ColorPaper(n // 2, cp, x + n // 2, y)
    cp4 = ColorPaper(n // 2, cp, x + n // 2, y + n // 2)

    if cp1 == cp2 == cp3 == cp4 and len(cp1) == 1 :
        return cp1

    return cp1+cp2+cp3+cp4


if __name__ == "__main__":
    n = int(input())
    arr = [input().split() for _ in range(n)]
    result = ColorPaper(n, arr, 0, 0)
    print(result.count('0'), result.count('1'), sep='\n')
