
n = int(input())
a = list(map(int, input().split()))
unique_entries = set()
for i in range(len(a)-1, -1, -1):
    if a[i] in unique_entries:
        a[i] = 0
    else:
        unique_entries.add(a[i])
x = len(unique_entries)
a = list(filter(lambda x: x != 0, a))
print(x)
print(' '.join(map(str, a)))

