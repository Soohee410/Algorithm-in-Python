from sys import stdin, stdout

_ = stdin.readline()
nums = list(map(int, stdin.readline().split()))

crd = {val:idx for idx,val in enumerate(sorted(set(nums)))}
stdout.write(' '.join([str(crd[i]) for i in nums]))
