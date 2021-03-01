# 이렇게 하면 속도 느림.
# 어떻게 빨리 할지 고민하기.

def TripleSix(N):
  num, count = 666, 0
  while True:
    if '666' in str(num): count += 1
    if count == N: return num
    num += 1

print(TripleSix(int(input())))
