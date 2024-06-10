
s = input()

if s[0:2] in ["01", "03", "05", "07", "08", "10", "12"] and 1 <= int(s[2:4]) <= 31:
    print("YYMM")
elif s[0:2] in ["04", "06", "09", "11"] and 1 <= int(s[2:4]) <= 30:
    print("YYMM")
elif s[0:2] in ["02"] and 1 <= int(s[2:4]) <= 29:
    print("YYMM")
elif s[2:4] in ["01", "03", "05", "07", "08", "10", "12"] and 1 <= int(s[0:2]) <= 31:
    print("MMYY")
elif s[2:4] in ["04", "06", "09", "11"] and 1 <= int(s[0:2]) <= 30:
    print("MMYY")
elif s[2:4] in ["02"] and 1 <= int(s[0:2]) <= 29:
    print("MMYY")
elif s[0:2] in ["02"] and 1 <= int(s[2:4]) <= 28:
    print("AMBIGUOUS")
elif s[2:4] in ["02"] and 1 <= int(s[0:2]) <= 28:
    print("AMBIGUOUS")
else:
    print("NA")

