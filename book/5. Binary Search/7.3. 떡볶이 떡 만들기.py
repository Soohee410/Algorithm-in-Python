from sys import stdin

N,M = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

start = 0
end = max(data)
result = 0

while(start <= end):
  total = 0
  mid = (start+end)//2
  for x in data:
    if x > mid:
      total += x-mid

  if total < M:       # 떡의 양이 부족한 경우
    end = mid - 1

  else:               # 떡의 양이 초과한 경우
    result = mid
    start = mid + 1

print(result)
