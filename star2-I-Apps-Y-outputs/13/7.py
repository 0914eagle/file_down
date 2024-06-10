
n = int(input())
s = input()

left = set()
right = set()

for i in range(n):
    if i < n // 2:
        left.add(s[i])
    else:
        right.add(s[i])

print(len(left.intersection(right)))

