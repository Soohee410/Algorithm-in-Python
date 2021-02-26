# First answer : 28776KB / 412ms
while True:
  stk = []
  words = list(input())
  if len(words)==1 and words[0]=='.' : break

  for i in words:
    if i=='(' or i==')' : stk.append(i)

    elif i == ')':
      if len(stk)>0 and stk[-1] =='(' : stk.pop()
      else: stk.append(i); break

    elif i == ']':
      if len(stk)>0 and stk[-1] =='[' : stk.pop()
      else: stk.append(i); break

  if len(stk) == 0 : print('yes')
  else: print('no')


# ---------------------------------------------------------
# Second answer: 28776KB / 92ms
from sys import stdin, stdout

def left(right):
  return '(' if right==')' else '['

def isBalanced(s):
  stk = []
  for i in s:
    if i in '([': stk.append(i)

    elif i in ')]':
      if not stk or stk[-1] != left(i): return False
      else: stk.pop()

  return not stk

while True:
  s = stdin.readline().rstrip()
  if s == '.': break
  stdout.write('yes\n' if isBalanced(s) else 'no\n')
