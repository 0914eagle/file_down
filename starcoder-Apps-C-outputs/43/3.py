
s = raw_input()

num_1 = "1"
num_6 = "6"
num_8 = "8"
num_9 = "9"

num = ""

for i in range(len(s)):
    if num_1 in s[i]:
        num = num + num_1
        s = s[:i] + s[i+1:]
        break

for i in range(len(s)):
    if num_6 in s[i]:
        num = num + num_6
        s = s[:i] + s[i+1:]
        break

for i in range(len(s)):
    if num_8 in s[i]:
        num = num + num_8
        s = s[:i] + s[i+1:]
        break

for i in range(len(s)):
    if num_9 in s[i]:
        num = num + num_9
        s = s[:i] + s[i+1:]
        break

for i in range(len(s)):
    num = num + s[i]

if (int(num)) % 7 == 0:
    print(num)
else:
    print("0")
