
n = int(input())
sheet = set()
for _ in range(n):
    a = int(input())
    if a in sheet:
        sheet.remove(a)
    else:
        sheet.add(a)
print(len(sheet))

