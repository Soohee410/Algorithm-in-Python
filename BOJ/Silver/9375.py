from sys import stdin

def Solution():
    n = int(stdin.readline())
    closet = dict()

    if n == 0: return 0

    for _ in range(n):
        kind = stdin.readline().split()[1]
        if kind not in closet.keys():
            closet[kind] = 1
        else:
            closet[kind] += 1

        result = 1
        for i in closet.values():
            result *= (i+1)

    return result-1


T = int(stdin.readline())
for _ in range(T):
    print(Solution())
