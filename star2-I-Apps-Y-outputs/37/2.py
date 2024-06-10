
n = int(input())
a = [int(input()) for _ in range(n)]

sheet = set()
for num in a:
    if num in sheet:
        sheet.remove(num)
    else:
        sheet.add(num)

print(len(sheet))

