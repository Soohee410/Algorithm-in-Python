# First Solution
import sys
input = sys.stdin.readline

def Solution():
    N = int(input().rstrip())
    M = int(input().rstrip())
    S = input().rstrip()

    cnt, ans, i = 0, 0, 0

    while i < M - 2:
        if S[i:(i+3)] == "IOI":
            cnt += 1
            if cnt == N:
                cnt -= 1
                ans += 1
            i += 2   # 한칸씩 볼 필요 X
        else:
            cnt = 0
            i += 1

    print(ans)

Solution()

# -------------------------------
# More advanced solution
# 정규표현식 모듈 이용
import re

n = int(input())
_ = input()
string = input()

ioi = re.findall('I(?:OI)+', string) #I(OI)*반복 이 들어간 문자열들 추출
count = 0

for k in ioi:
	c = len(k) // 2 - n + 1
	if c > 0:
		count += c

print(count)
