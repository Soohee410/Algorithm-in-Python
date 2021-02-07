n = int(input())
x,y = 1,1
plans = input().split()

move_types = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dx[i]

    #공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue

    x,y = nx,ny

print(x, y)
