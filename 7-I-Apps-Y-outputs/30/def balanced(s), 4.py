
def balanced(s):
    count = [0,0,0]
    for i in s:
        count[int(i)] += 1
    if count[0] == count[1] and count[1] == count[2]:
        return s
    if count[0] < count[1] or count[1] < count[2]:
        return "Impossible"
    if count[0] > count[1] or count[1] > count[2]:
        if count[0] > count[2]:
            return "".join(["0" for i in range(count[0] - count[2])] + ["2" for i in range(count[2])] + ["1" for i in range(count[1])])
        else:
            return "".join(["2" for i in range(count[2] - count[0])] + ["0" for i in range(count[0])] + ["1" for i in range(count[1])])

n = int(input())
s = input()
print(balanced(s))

