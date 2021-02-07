# nC2에서 무게 같은 공들의 조합 개수 빼기

N,M = map(int, input().split())
balls = list(map(int, input().split()))

count = {}

def comb(n):
    return n*(n-1)/2

result = comb(N) #전체 조합 개수

for i in balls:
    try: count[i] += 1
    except: count[i] = 1

for j in count.values():
    if j>1:
        result -= comb(j)

print(int(result))
