# Solution
def solution(numbers, target):
    answer = 0
    que = deque([(0,0)])
    n = len(numbers)

    while que:
        summ, idx = que.popleft()

        if idx == n and summ == target:
            answer += 1
            continue

        if idx < n:
            que.append((summ + numbers[idx], idx+1))
            que.append((summ - numbers[idx], idx+1))

    return answer


    # -------------------------------------------
    # More simpler solution

    def solution(numbers, target):
        if not numbers and target == 0 :
            return 1

        elif not numbers:
            return 0

        else:
            return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
