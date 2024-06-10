
s = input()
t = input()

for i in range(len(s)):
    if s == t:
        print("Yes")
        break
    else:
        s = s[-1] + s[:-1]
    if i == len(s) - 1:
        print("No")

