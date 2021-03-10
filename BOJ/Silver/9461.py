from sys import stdin,stdout
T = int(stdin.readline())
Ns = [int(stdin.readline()) for _ in range(T)]

d = [1,1,1] + [2,2] + [0]*95
for i in range(5,max(Ns)):
    d[i] = d[i-1] + d[i-5]

stdout.write('\n'.join([str(d[j-1]) for j in Ns]))
