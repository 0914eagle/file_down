
s = input()

pivot = s.index('^')

left = 0
right = 0

for i in range(pivot):
    if s[i].isdigit():
        left += int(s[i])

for i in range(pivot+1,len(s)):
    if s[i].isdigit():
        right += int(s[i])

if left==right:
    print("balance")
elif left<right:
    print("right")
else:
    print("left")
