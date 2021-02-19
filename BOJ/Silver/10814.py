import sys

N = int(sys.stdin.readline())

members = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

members.sort(key = lambda x: x[0])

for age,name in members: print(age, name)
