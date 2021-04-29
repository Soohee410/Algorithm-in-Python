#Solution1

def solution(numbers):
    numbers = list(map(str, numbers))

    #각 수들을 여러번 중복한 값들의 str을 정렬한다.
    #str을 정렬할 경우, 첫 글자부터 차례로 기준으로 삼아 정렬.
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(numbers))) # '0000' --> '0'을 위한 str(int())



#------------------------------------------------------
#Solution2

import functools

#비교 함수
#비교 함수는 a,b를 받아, a가 b보다 작으면 음수, 같으면 0, 크면 양수를 반환하는 콜러블.
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크면 1, 작으면 -1,  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key = functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer
