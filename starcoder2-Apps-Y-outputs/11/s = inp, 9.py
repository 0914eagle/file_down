
s = input()
n = int(input())

count = 0
max = 0

for i in range(n-1):
    for j in range(i+1, n):
        if s[i] == s[j]:
            count += 1
            if count > max:
                max = count
                ans = s[i:j+1]
        else:
            count = 0

print(ans)

