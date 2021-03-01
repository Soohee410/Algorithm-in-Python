def Minecraft(data,B):
  sec, H = float('Inf'), 0
  minimum, maximum = min(data), max(data)

  for h in range(minimum, min(maximum+1,257)):
    fill, tmp = 0, 0
    B_fill = B

    for x,num in data.items():
      if x<h:                    # 높이보다 작으면,
        fill += (h-x)*num        # B에서 가져와야 할 개수 추가.
        tmp += (h-x)*num         # 시간 계산 (1초)
      else:                      # 높이보다 크면,
        tmp += 2*(x-h)*num       # 시간 계산 (2초)
        B_fill += (x-h)*num      # B에 남는 부분 추가해줄 수 있음.

    if fill > B_fill: continue

    if tmp <= sec:              # 시간이 짧을수록, 높이는 클수록 저장.
      sec = tmp
      H = h

  return sec,H



from sys import stdin
from collections import Counter

N, _, B = map(int, stdin.readline().split())
data = []
for _ in range(N):
  data += list(map(int, stdin.readline().split()))
data = Counter(data)

sec, H = Minecraft(data,B)
print(sec,H)
