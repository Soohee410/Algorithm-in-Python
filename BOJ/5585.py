N = int(input())
money = 1000-N
coins = [500,100,50,10,5,1]

count = 0
for i in coins:
    count += money//i; money=money%i

print(count)
