

# -*- coding: utf-8 -*-

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = "YES\n"

for i in range(n):
    result += " ".join(list(map(str, range(1, a[i] + 1)))) + "\n"

print(result)

