
h = int(input())
hotdogs = list(map(int, input().split()))
b = int(input())
buns = list(map(int, input().split()))
hotdogs.sort(reverse=True)
buns.sort(reverse=True)
total = 0
for i in range(min(h, b)):
    if hotdogs[i] == buns[i]:
        total += 1
    elif hotdogs[i] < buns[i]:
        total += buns[i] // hotdogs[i]
    else:
        total += hotdogs[i] // buns[i]
print(total)

