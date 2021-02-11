N = int(input())
num = N//5
count = 0
for i in range(num,-1,-1):
    if (N-5*i)%3==0:
        count = i + (N-5*i)//3
        break
    else:
        continue
if count == 0: count = -1
print(count)
