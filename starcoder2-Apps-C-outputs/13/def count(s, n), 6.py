
s = input()
n = len(s)

def count(s, n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] == s[j:j+1]*(j-i+1):
                count += 1
    return count

print(count(s, n))
