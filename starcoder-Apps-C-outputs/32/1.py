
s = input()
res = 'YES'
counta = 0
countb = 0
countc = 0
for i in s:
    if i == 'a':
        counta += 1
    elif i == 'b':
        countb += 1
    elif i == 'c':
        countc += 1
if (counta != countc and countb != countc and counta != countb):
    res = 'NO'
print(res)
