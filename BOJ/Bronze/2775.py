#재귀함수로 하니까 시간초과 떴음ㅠ
T = int(input())

for _ in range(T):
    reside = []
    k = int(input())
    n = int(input())
    reside = [i for i in range(1, n+1)]

    for _ in range(k):
        for j in range(1, n):
            reside[j] += reside[j-1]
            
    print(reside[-1])
