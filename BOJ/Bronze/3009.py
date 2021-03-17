# Solution1
def Unique(nums):
    mean = sum(nums)/3
    tmp = [abs(i-mean) for i in nums]
    return nums[tmp.index(max(tmp))]

xx, yy = [], []
for _ in range(3):
    x,y = map(int, input().split())
    xx.append(x)
    yy.append(y)

print(Unique(xx), Unique(yy))


# ---------------------------
# Solution2 : 비트 연산자
x=y=0

for _ in range(3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b

print(x, y)
