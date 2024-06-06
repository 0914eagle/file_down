
n = int(input())
s = input()
m = 0
for c in s:
    if m < ord(c) - ord('a') + 1:
        m = ord(c) - ord('a') + 1
print(m)
