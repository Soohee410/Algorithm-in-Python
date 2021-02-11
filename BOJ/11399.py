N = int(input())
Pi = list(map(int, input().split()))
Pi.sort()

time = 0
for i in range(1,len(Pi)+1):
    time += sum(Pi[:i])
    
print(time)
