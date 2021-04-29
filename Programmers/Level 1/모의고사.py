def solution(answers):
    result = [[1,0], [2,0], [3,0]]
    n = len(answers)

    way = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    way_n = [len(x) for x in way]

    for i in range(n):
        for j in range(3):
            result[j][1] += int(way[j][i % way_n[j]] == answers[i])

    value = max(result, key = lambda x: x[1])[1]
    answer = [p for p, cnt in result if cnt == value]

    return answer
