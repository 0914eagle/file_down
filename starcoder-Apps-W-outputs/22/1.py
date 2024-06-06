
import sys

for line in sys.stdin:
    # print('Read: ', line, end='')
    str1 = line.strip()
    weight = 0
    left = 0
    right = 0
    pivot = False
    for i in str1:
        if i == "^":
            pivot = True
        elif i == "=":
            continue
        else:
            if pivot:
                right += int(i) * (len(str1) - 1 - int(str1.find(i)))
                pivot = False
            else:
                left += int(i) * int(str1.find(i))
    if left == right:
        print("balance")
    elif left > right:
        print("left")
    else:
        print("right")
