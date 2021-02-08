n = int(input())
ox_list = [input() for _ in range(n)]

def score(x):
    x_list = [len(i) for i in x.split('X')]
    result = 0
    for j in x_list:
        for k in range(1, j+1): result += k
    return result

for ox in ox_list:
    print(score(ox))
