#Solution
def solution(phone_book):
    data = sorted(phone_book, key = str.lower)

    for i in range(len(data)-1):
        if data[i+1].startswith(data[i]):
            return False

    return True


#--------------------------------------------------
#Another Solution by Hash
#element check 속도가 리스트보다 빠름.

def solution(phone_book):
    answer = True
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""

        for number in phone_number:
            temp += number

            if temp in hash_map and temp != phone_number:
                return False

    return True
