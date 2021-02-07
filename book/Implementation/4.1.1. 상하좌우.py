n = int(input())
min_n = 1; max_n=n

plan = list(map(str, input().split(' ')))

x,y = min_n, min_n

for i in plan:
    if i == 'L':
        if y==min_n:
            y = y
        else:
            y -= 1

    elif i == 'R':
        if y==max_n:
            y = y
        else:
            y += 1

    elif i == 'U':
        if x==min_n:
            x = x
        else:
            x -= 1

    else:
        if x==max_n:
            x = x
        else:
            x += 1

print(x, y)
