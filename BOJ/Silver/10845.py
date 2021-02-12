from collections import deque
class queue:
  def __init__(self):
    self.queue = deque([])

  def size(self):
    return len(self.queue)

  def empty(self):
    if self.size()==0: return 1
    else: return 0

  def push(self, value):
    self.queue.append(value)

  def pop(self):
    if self.empty() == 1: return -1
    else: return self.queue.popleft()

  def front(self):
    if self.empty() == 1: return -1
    else: return self.queue[0]

  def back(self):
    if self.empty() == 1: return -1
    else: return self.queue[-1]

import sys
N = int(input())
cmd_list = [list(sys.stdin.readline().split()) for _ in range(N)]

que = queue()
for cmd in cmd_list:
    word = cmd[0]
    if len(cmd) ==2: que.push(int(cmd[1]))
    elif word == 'pop': print(que.pop())
    elif word == 'size': print(que.size())
    elif word == 'empty': print(que.empty())
    elif word == 'front': print(que.front())
    else: print(que.back())
