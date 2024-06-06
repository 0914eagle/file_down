
s = input()
vowels = 'AEIOUYaeiouy'
def count(s):
    c = 1
    for i in range(1,len(s)-1):
        if s[i].upper() in vowels:
            if s[i-1:i+2].upper() == 'Q' or (s[i-1:i+2].upper() == 'Y' and s[i+2].upper() not in vowels):
                c+=1
    return c

s = s.split(' ')
res = ['','','']
l = [0,0,0]
j = 0
for i in s:
    cnt = count(i)
    l[j] += cnt
    if l[j] > 7:
        j+=1
    if j > 2:
        break
    res[j]+=i+' '
if l[0] == 5 and l[1] == 7 and l[2] == 5:
    print(res[0])
    print(res[1])
    print(res[2])
else:
    print(s)
