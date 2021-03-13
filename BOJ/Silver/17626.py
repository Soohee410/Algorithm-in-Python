def FourSquares(x):
    result = 4

    for i in range(int(n**0.5), int((n//2)**0.5)-1, -1):  #절반의 루트값 이하까지 보면, 그 다음 for문에서 중복됨.
        a = n - i*i
        if a == 0: return 1

        for j in range(int(a**0.5), int((a//2)**0.5)-1, -1):
            b = a - j*j
            if b == 0:
                result = min(result, 2)
                break

            for k in range(int(b**0.5), int((b//2)**0.5)-1, -1):
                c = b - k*k
                if c == 0:
                    result = min(result, 3)
                    break

    return result


n = int(input())
print(FourSquares(n))
