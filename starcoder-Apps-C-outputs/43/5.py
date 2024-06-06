
a = input()
s = set(a)
if "0" in s:
    print(0)
elif len(a) > 4 and "7" in s:
    a = a.replace("7", "")
    print(7 * int(a))
else:
    a = a.replace("1", "")
    a = a.replace("6", "")
    a = a.replace("8", "")
    a = a.replace("9", "")
    print(7 * int(a))
