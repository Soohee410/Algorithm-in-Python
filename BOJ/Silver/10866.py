from collections import deque

class Deque:
  def __init__(self):
    self.deq = deque([])

  def size(self):
    return len(self.deq)

  def empty(self):
    if self.size()==0: return 1
    else: return 0

  def push_front(self, value):
    self.deq.appendleft(value)

  def push_back(self, value):
    self.deq.append(value)

  def pop_front(self):
    if self.empty() == 1: return -1
    else: return self.deq.popleft()

  def pop_back(self):
    if self.empty() == 1: return -1
    else: return self.deq.pop()

  def front(self):
    if self.empty() == 1: return -1
    else: return self.deq[0]

  def back(self):
    if self.empty() == 1: return -1
    else: return self.deq[-1]

import sys
N = int(input())
cmd_list = [list(sys.stdin.readline().split()) for _ in range(N)]

deq = Deque()
for cmd in cmd_list:
    word = cmd[0]
    if word == 'push_front': deq.push_front(int(cmd[1]))
    elif word == 'push_back': deq.push_back(int(cmd[1]))
    elif word == 'pop_front': print(deq.pop_front())
    elif word == 'pop_back': print(deq.pop_back())
    elif word == 'size': print(deq.size())
    elif word == 'empty': print(deq.empty())
    elif word == 'front': print(deq.front())
    else: print(deq.back())
