from sys import stdin,stdout

def isVPS(s):
  stk = []
  for i in s:
    if i =='(': stk.append(i)
    elif stk and i==')': stk.pop()
    else: return False
  return not stk

T = int(stdin.readline())

for _ in range(T):
  s = stdin.readline().rstrip()
  stdout.write('YES\n' if isVPS(s) else 'NO\n')
