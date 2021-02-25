# Using deque
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
  N,M = map(int, sys.stdin.readline().split())
  que = deque(map(int, sys.stdin.readline().split()))  # 덱으로 저장.
  result = 0

  while True:
    M -= 1
    maximum = max(que)
    temp = que.popleft()

    if temp != maximum:  # 뽑은 값이 최대가 아닌 경우,
      que.append(temp)
      if M == -1:        # M이 -1이면,
        M = len(que)-1   # 뒤로 보내고 M을 다시 맨 뒤 인덱스로 할당.

    else:                # 뽑은 값이 최대인 경우,
      result += 1
      if M == -1:        # M이 -1이면, 횟수 출력.
        print(result)
        break


# ------------------
# Using list : 메모리와 시간이 더 단축됐음.

import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N,M = map(int, sys.stdin.readline().split())
  que = list(map(int, sys.stdin.readline().split()))   # 리스트로 저장.
  result = 0

  while True:
    M -= 1
    maximum = max(que)
    temp = que.pop(0)     #deque과의 차이는 pop(0) 밖에 없음.

    if temp != maximum:
      que.append(temp)
      if M == -1:
        M = len(que)-1

    else:
      result += 1
      if M == -1:
        print(result)
        break
