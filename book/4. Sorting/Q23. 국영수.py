import sys

N = int(sys.stdin.readline())
std_list = []

for _ in range(N):
  std = sys.stdin.readline().split()
  std_list.append((std[0],int(std[1]), int(std[2]),int(std[3])))

std_list = sorted(std_list, key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in std_list: sys.stdout.write(i[0]+'\n')
