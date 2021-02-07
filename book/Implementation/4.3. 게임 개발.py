#왼쪽으로 먼저 돈 뒤에 전진하는게 잘 드러나지 않음.
#개수는 나오긴 나오나 보완 필요,,

N,M = map(int, input().split())
A,B,d = map(int, input().split())
Map = [list(map(int, input().split())) for i in range(M)]

d_list = [0,3,2,1] #북-서-남-동
move = [(0,-1),(1,0),(0,1),(-1,0)] #서-남-동-북
d_idx = d_list.index(d)

a = 0 #네방향 중 가본 칸이거나 바다로 되어 있는 칸의 개수
count = 1

while True:
    Map[A][B] = 2

    for d,j in zip(d_list[d_idx:]+d_list[:d_idx], move[d_idx:]+move[:d_idx]):
        if Map[A+j[0]][B+j[1]] == 0:
            A = A+j[0]
            B = B+j[1]
            Map[A][B] = 2 #가본 칸은 2로 설정
            count += 1
            a = 0
            break
        else:
            a += 1

    d_idx = d_list.index(d)

    if a==4:
        back = move[(d_idx+1)%4]
        if Map[A+back[0]][B+back[1]] == 1:
            break
        else:
            A = A+back[0]
            B = B+back[1]


    a = 0 #reset a

print(count)
