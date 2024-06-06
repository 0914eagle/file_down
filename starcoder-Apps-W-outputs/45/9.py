
s1 = input()
s2 = input()

res = 0

def s2d(s2):
    if len(s2)==0:
        return 1
    if s2[0] != '?':
        return s2d(s2[1:]) * 1 if s2[0]=='+' else -1
    else:
        return s2d(s2[1:]) * 0.5 + s2d(s2[1:]) * 0.5

for i in range(len(s1)):
    if s1[i] == s2[i]:
        res += s2d(s2[i+1:])

print(res/pow(2, len(s2)))
