S = list(input())
string = []; nums = []
for i in S:
    try: nums.append(int(i))
    except: string.append(i)

string.sort()
if len(nums)!=0:
    string.append(str(sum(nums)))

print(''.join(string))
