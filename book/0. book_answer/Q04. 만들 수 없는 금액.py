#target보다 새 화폐가 크면, target을 못 만들게 됨.

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for i in coins:
    if target < i: break
    target += i

print(target)
