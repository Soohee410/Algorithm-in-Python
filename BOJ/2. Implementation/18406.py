N = input()
mid = int(len(N)/2)
left = sum(list(map(int, N[:mid])))
right = sum(list(map(int, N[mid:])))
result = "LUCKY" if left==right else "READY"
print(result)
