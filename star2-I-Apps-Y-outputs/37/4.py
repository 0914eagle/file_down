
N = int(input())
A = [int(input()) for _ in range(N)]

sheet = set()
for a in A:
    if a in sheet:
        sheet.remove(a)
    else:
        sheet.add(a)

print(len(sheet))

