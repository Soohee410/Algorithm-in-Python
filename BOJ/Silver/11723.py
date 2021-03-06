from sys import stdin


class Set:
    def __init__(self):
        self.set = set()

    def add(self, value):
        self.set.add(value)

    def check(self, value):
        if value in self.set: return 1
        else: return 0

    def remove(self, value):
        if self.check(value) == 1:
          self.set.remove(value)

    def toggle(self, value):
        if self.check(value) == 1: self.remove(value)
        else: self.add(value)

    def all(self):
        self.set = set(range(1, 21))

    def empty(self):
        self.set.clear()


M = int(stdin.readline())
S = Set()
for _ in range(M):
    cmd = list(stdin.readline().split())
    if cmd[0] == 'add':
        S.add(int(cmd[1]))
    elif cmd[0] == 'check':
        print(S.check(int(cmd[1])))
    elif cmd[0] == 'remove':
        S.remove(int(cmd[1]))
    elif cmd[0] == 'toggle':
        S.toggle(int(cmd[1]))
    elif cmd[0] == 'all':
        S.all()
    else:
        S.empty()
