
n, k = map(int, input().split())
groups = input().split()

names = []
for i in range(n):
    if i < k-1:
        names.append("A")
    elif i == k-1:
        if groups[0] == "YES":
            names.append("B")
        else:
            names.append("A")
    else:
        if groups[i-k+1] == "YES":
            names.append(chr(ord(names[i-k]) + 1))
        else:
            names.append(names[i-k])

print(" ".join(names))
