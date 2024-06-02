
n = int(input())
s = input()

d = {}
for i in range(n-1):
    if s[i:i+2] in d:
        d[s[i:i+2]] += 1
    else:
        d[s[i:i+2]] = 1

max_val = max(d.values())
for key in d:
    if d[key] == max_val:
        print(key)
        break

