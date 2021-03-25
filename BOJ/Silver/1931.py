from sys import stdin

N = int(stdin.readline())
data = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
data.sort(key=lambda x: (x[1],x[0]))

cnt = 0
end_old = 0
for start, end in data:
    if start >= end_old:
        cnt += 1
        end_old = end

print(cnt)
