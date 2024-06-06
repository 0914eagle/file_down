
a = input()
a = list(a)
if "1" in a and "6" in a and "8" in a and "9" in a:
    b = []
    for i in range(len(a)):
        if a[i] == "1":
            b.append(a[i])
        if a[i] == "6":
            b.append(a[i])
        if a[i] == "8":
            b.append(a[i])
        if a[i] == "9":
            b.append(a[i])
    b.sort(reverse=True)
    res = ""
    for i in b:
        res += i
    print(res)
else:
    print("0")
