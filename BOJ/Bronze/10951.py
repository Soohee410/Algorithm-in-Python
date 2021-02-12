sum_list = []

while True:
    try:
        A,B = map(int, input().split())
        sum_list.append(A+B)
    except:
        break
for i in sum_list:
    print(i)
