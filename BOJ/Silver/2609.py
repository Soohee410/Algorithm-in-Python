#최대공약수는 유클리드 호제법으로 풀기! log(N)
def euclid(x,y): #x>y
    if y == 0: return x
    return euclid(y, x%y)

A, B = map(int, input().split())
n1 = euclid(max(A,B), min(A,B))
n2 = round(A*B/n1)
print(n1); print(n2)
