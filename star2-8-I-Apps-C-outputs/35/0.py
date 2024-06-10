
n = int(input())
print((4 * n + 4) - 8)
for i in range(1, 5 * n + 5, 2):
    if i not in (2, 4 * n + 2, 4 * n + 4, 8 * n + 4):
        print(i, end=" ")
print()

