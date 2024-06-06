
a = str(input())
b = str(input())
if len(a) != len(b):
    print("NO")
    exit()
for i in range(len(a)):
    if a[i] == "0":
        if b[i] == "0":
            continue
        else:
            print("NO")
            exit()
    if a[i] == "1":
        if b[i] == "1":
            continue
        else:
            print("NO")
            exit()
print("YES")
