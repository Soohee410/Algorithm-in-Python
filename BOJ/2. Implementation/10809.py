S = list(input())

alphabet = [-1]*26
for loc,i in enumerate(S):
    if alphabet[ord(i)-97] == -1:
        alphabet[ord(i)-97] = loc

for j in alphabet: print(j, end=' ')
