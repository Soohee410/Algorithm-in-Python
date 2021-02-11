T = int(input())

RS_list = []
for _ in range(T):
    R, S = input().split()
    temp = [i*int(R) for i in list(S)]
    RS_list.append(''.join(temp))

for i in RS_list:
    print(i)
