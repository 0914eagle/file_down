
def balanced(s):
    count = [0,0,0]
    for i in s:
        count[int(i)] += 1
    if count[0] == count[1] and count[1] == count[2]:
        return s
    else:
        if count[0] > count[1]:
            if count[0] > count[2]:
                return s.replace('0','2',count[0]-count[1])
            else:
                return s.replace('0','1',count[0]-count[1])
        else:
            if count[1] > count[2]:
                return s.replace('1','2',count[1]-count[2])
            else:
                return s.replace('1','0',count[1]-count[2])

n = int(input())
s = input()
print(balanced(s))

