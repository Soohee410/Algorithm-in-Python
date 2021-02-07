x,y = input()
x = ord(x)
y = int(y)

move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

count = 0
for dx, dy in move:
    nx = x + dx
    ny = y + dy

    if nx <ord('a') or ny<1 or nx>ord('h') or ny>8:
        continue

    count += 1

print(count)
