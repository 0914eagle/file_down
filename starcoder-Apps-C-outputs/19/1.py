
def _solve():
    x = input()
    y = input()
    x = x.split(":")
    y = y.split(":")
    ans = []
    if int(x[0]) == int(y[0]) and int(x[1]) == int(y[1]):
        ans.append(x[0] + ":" + x[1])
        return ans

    if int(x[1]) == int(y[1]):
        if int(y[0]) - int(x[0]) < 10:
            ans.append(x[0] + ":" + x[1])
            ans.append(str(int(x[0]) + 1) + ":" + x[1])
            ans.append(y[0] + ":" + y[1])
            return ans
        else:
            ans.append(x[0] + ":" + x[1])
            ans.append(str(int(x[0]) - 1) + ":" + x[1])
            ans.append(y[0] + ":" + y[1])
            return ans
    else:
        for i in range(int(y[1]) - int(x[1])):
            x[1] = int(x[1]) + 1
            if int(x[1]) == 10:
                x[1] = "00"
            else:
                x[1] = "0" + str(x[1])
        ans.append(x[0] + ":" + x[1])
        return ans

if __name__ == "__main__":
    print(len(_solve()))
    for i in _solve():
        print(i)
