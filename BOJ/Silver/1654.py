from sys import stdin

def BS_line(data,N):
    start, end = 1, max(data)
    result = 0

    while start<= end:
        total = 0
        mid = (start+end)//2
        total = sum([x//mid for x in data])

        if total < N:         # 랜선 개수가 N보다 적을 경우,
            end = mid -1      # 보다 짧은 길이 (왼쪽) 탐색.
        else:                 # 랜선 개수가 N 이상일 경우,
            result = mid      # result에 일단 할당.
            start = mid + 1   # 보다 긴 길이 (오른쪽) 탐색.

    return result


K,N = map(int, stdin.readline().split())
data = [int(stdin.readline()) for _ in range(K)]
print(BS_line(data,N))
