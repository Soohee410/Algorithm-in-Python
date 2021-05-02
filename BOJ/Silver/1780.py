# Solution1
# 373800KB / 3988ms
from itertools import product
from collections import Counter

def TripleTree(n, arr, x, y):
    if n == 1:
        return arr[x][y]
    n = n//3
    cp = [0] * 9
    for k,i in enumerate(list(product([0,1,2], repeat=2))):
        cp[k] = TripleTree(n, arr, x+n*i[0], y+n*i[1])

    if len(set(cp)) == 1 and (len(cp[0]) == 1 or cp[0] == '-1'):
        return cp[0]

    return ' '.join(cp)


if __name__ == "__main__":
    n = int(input())
    arr = [input().split() for _ in range(n)]
    res = TripleTree(n, arr, 0, 0)
    cnt = Counter(res.split())
    print(cnt['-1'], cnt['0'], cnt['1'], sep='\n')


# ----------------------------
# arr 받을 때, -1을 2로 대체하여 받으면,
# 결과 split해서 리스트로 바꾸고 그럴 필요 없고, 메모리/시간 모두 아낄 수 있음.
# 76788KB / 3152ms
def TripleTree(n, arr, x, y):
    if n == 1:
        return arr[x][y]

    n = n//3
    cp = []
    for k,i in enumerate(list(product([0,1,2], repeat=2))):
        cp.append(TripleTree(n, arr, x+n*i[0], y+n*i[1]))

    if len(set(cp)) == 1 and len(cp[0]) == 1:
        return cp[0]

    return ''.join(cp)


if __name__ == "__main__":
    n = int(input())
    arr = [input().replace('-1','2').split() for _ in range(n)]
    res = TripleTree(n, arr, 0, 0)
    print(res.count('2'), res.count('0'), res.count('1'), sep='\n')
