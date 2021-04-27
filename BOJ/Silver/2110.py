import sys
input = sys.stdin.readline

def BS_search(data,n,c):
    start = 1
    end = data[n-1] - data[0]
    result = 0

    if c == 2: return end

    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        before = data[0]

        for i in range(1, n):
            if data[i] >= before + mid:
                before = data[i]
                cnt += 1

        if cnt < c:  #mid가 너무 크다는 뜻.
            end = mid - 1
        else:  #mid가 작거나 적당하다는 뜻.
            start = mid + 1
            result = mid

    return result


def Solution():
    n, c = map(int, input().split())
    data = [int(input()) for _ in range(n)]
    data.sort()
    print(BS_search(data,n,c))

Solution()
