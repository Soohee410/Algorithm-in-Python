# First Solution: 36588KB / 512ms
def Solution(x):
    d = [0] * 30001
    for i in range(2,x+1):
        d[i] = d[i-1] + 1
        if i%2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)

    print(d[x])

Solution(int(input()))


# --------------------------------------
# Advanced Solution: 28776KB / 72ms

def DP(x):
    if x in d:
        return d[x]

    d[x] = 1 + min(DP(x//2) + x%2, DP(x//3) + x%3)

    return d[x]


d = {1: 0, 2: 1}

print(DP(int(input())))
