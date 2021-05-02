def QuadTree(n, cp, x, y):
    if n == 1:
        return cp[x][y]

    cp1 = QuadTree(n // 2, cp, x, y)
    cp2 = QuadTree(n // 2, cp, x, y + n // 2)
    cp3 = QuadTree(n // 2, cp, x + n // 2, y)
    cp4 = QuadTree(n // 2, cp, x + n // 2, y + n // 2)

    if cp1 == cp2 == cp3 == cp4 and len(cp1) == 1:
        return cp1

    return '('+cp1+cp2+cp3+cp4+')'


if __name__ == "__main__":
    n = int(input())
    arr = [list(input().rstrip()) for _ in range(n)]
    print(QuadTree(n, arr, 0, 0))
