
def rotate(s):
    return s[-1] + s[:-1]

s = input()
t = input()

for _ in range(len(s)):
    if s == t:
        print('Yes')
        break
    s = rotate(s)
else:
    print('No')

