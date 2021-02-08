word = input()
word_list = list(word.upper())

from collections import Counter

if len(word_list)==1: print(word_list[0])
else:
    A = Counter(word_list)
    B = A.most_common(2)
    if B[0][1] == B[1][1]: print('?')
    else: print(B[0][0])
