#모든 음식이 0이 아닌 상황에서, 0이 아닌 음식 만날 때까지 이동.
#모든 음식이 0이면 반복문 중단.

#오답
def solution(food_times, k):
    answer = 0
    length = len(food_times)

    for i in range(k):

        while sum(food_times)>0:
            answer += 1
            answer %= length
            if food_times[answer]!=0: break

        if sum(food_times)==0:
            answer = 0
            break

        food_times[answer] -= 1

    return answer+1
