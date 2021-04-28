#정렬
def solution(array, commands):
    answer = []
    n = len(array)

    for num in range(len(commands)):
        i, j, k = commands[num]
        tmp = sorted(array[i-1 : j])
        answer.append(tmp[k-1])

    return answer
