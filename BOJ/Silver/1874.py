# 첫번째 답: 35664KB / 220ms
from sys import stdin

def StackSequence(data):
  stk, result, maximum = [], [], data[0]
  for i in range(1,maximum+1):
    stk.append(i); result.append('+')
  stk.pop(); result.append('-')

  for x in data[1:]:
    if x > maximum:
      for j in range(maximum+1,x+1):
        stk.append(j); result.append('+')
      stk.pop(); result.append('-')
      maximum = x

    else:
      if not stk: return False
      else:
        while stk:
          tmp = stk.pop()
          result.append('-')
          if tmp == x: break
        if not stk and tmp!=x: return False

  return '\n'.join(result)


n = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(n)]
print(StackSequence(data))


# -------------------------------------------------------------------------
# 발전된 답
from sys import stdin

def StackSequence(data):
  stk, result, num = [], [], 1    # num은 포인터? 커서? 라고 생각하자

  for x in data:
    while num <= x:               # x가 현재 커서(값)보다 클 경우
      stk.append(num)             # x까지의 값 추가
      result.append('+')
      num += 1                    # 커서 이동

    if stk.pop() != x:            # pop을 했는데 x가 아닐 경우 NO
      return 'NO'
    else:
      result.append('-')

  return '\n'.join(result)


n = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(n)]

print(StackSequence(data))
