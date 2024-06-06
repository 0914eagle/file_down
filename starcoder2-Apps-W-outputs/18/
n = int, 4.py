
n = int(input())
s = input()

if s.count('?') % 2 == 1:
    print("Monocarp")
else:
    if s.count('?') == 0:
        if int(s) % 2 == 0:
            print("Bicarp")
        else:
            print("Monocarp")
    else:
        print("Bicarp")
