
# 1
t = int(input())
for i in range(t):
    k = int(input())
    s = input()
    count = 0
    for j in range(len(s)):
        if s[j] == 'A':
            count += 1
    print(count)
