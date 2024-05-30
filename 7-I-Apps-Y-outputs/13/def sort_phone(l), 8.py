
def sort_phone(l):
    l = sorted(l)
    for i in l:
        if i[0] == '0':
            print('+91' + i[1:])
        elif i[0] == '9' or i[0] == '8':
            print('+91' + i)
        else:
            print(i)

n = int(input())
l = []
for i in range(n):
    l.append(input())
sort_phone(l)

