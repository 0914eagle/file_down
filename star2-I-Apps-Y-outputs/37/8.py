
n = int(input())
a = [int(input()) for _ in range(n)]

sheet = set()
for i in a:
    if i in sheet:
        sheet.remove(i)
    else:
        sheet.add(i)

print(len(sheet))

