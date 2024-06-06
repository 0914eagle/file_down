
a = input()
x = 0
for i in range(len(a)):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'o' or a[i] == 'u' or a[i] == 'i':
        x = 0
    elif a[i] == 'n':
        x = 0
    elif a[i-1] == 'n':
        x = 0
    else:
        x = 1
        break
if x == 0:
    print("YES")
else:
    print("NO")
