class stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.size()==0: return 1
        else: return 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.empty()==1: return -1
        else: return self.stack.pop()

    def top(self):
        if self.empty()==1: return -1
        else: return self.stack[-1]


import sys
N = int(input())
cmd_list = [list(sys.stdin.readline().split()) for _ in range(N)]

stk = stack()

for cmd in cmd_list:
    word = cmd[0]
    if len(cmd) == 2: stk.push(int(cmd[1]))
    elif word == 'pop': print(stk.pop())
    elif word == 'size': print(stk.size())
    elif word == 'empty': print(stk.empty())
    else: print(stk.top())
