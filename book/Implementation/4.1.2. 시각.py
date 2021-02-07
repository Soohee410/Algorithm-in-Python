N = int(input())

num =0
for hour in range(N+1):
    for minute in range(60):
        for sec in range(60):
            time = '%d%d%d' %(hour,minute,sec)
            if '3' in time:
                num += 1

print(num)
