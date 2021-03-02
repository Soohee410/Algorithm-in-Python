#Solution1: 62824KB / 284ms
# key:value, value:key 둘다 딕셔너리로 저장.

def Pokemon(data,test):
    data_key = {v:k for k,v in data.items()}
    result = []
    for i in test:
      try:
        result.append(data[int(i)])
      except:
        result.append(data_key[i])

    return result

from sys import stdin,stdout
N, M = map(int, stdin.readline().split())
data = {idx:stdin.readline().rstrip() for idx in range(1,N+1)}
test = [stdin.readline().rstrip() for x in range(M)]
stdout.write('\n'.join(map(str,Pokemon(data,test))))


# -----------------------------------------------------------
# Solution2: 55948KB / 332ms
# 하나는 딕셔너리, 하나는 리스트로 저장.

def Pokemon(data,test):
    data_key = {key:(idx+1) for idx,key in enumerate(data)}
    result = []
    for i in test:
      try:
        result.append(data[int(i)-1])
      except:
        result.append(data_key[i])
    return result

from sys import stdin,stdout
N, M = map(int, stdin.readline().split())
data = [stdin.readline().rstrip() for x in range(N)]
test = [stdin.readline().rstrip() for x in range(M)]
stdout.write('\n'.join(map(str,Pokemon(data,test))))
