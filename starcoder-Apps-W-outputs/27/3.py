
def check(arr, start, last):
    count = 0
    for i in range(start, last):
        if arr[i] > arr[i + 1]:
            count += 1
    if count >= 2:
        return False
    return True


def sort_string(string):
    if len(string) == 1:
        return string
    elif len(string) == 2:
        if string[0] > string[1]:
            string[0], string[1] = string[1], string[0]
        return string
    else:
        index = 0
        for i in range(0, len(string) - 1):
            if string[i] > string[i + 1]:
                index = i
                break
        if index == 0:
            return sort_string(string[1:]) + string[0]
        else:
            return sort_string(string[0:index]) + sort_string(string[index + 1:])


n = int(input())
arr = []
for _ in range(n):
    s = input()
    arr.append(s)
arr.sort()
flag = 0
for i in range(1, len(arr)):
    flag = 1
    if check(arr[i - 1], 0, len(arr[i - 1]) - 1) and check(arr[i], 0, len(arr[i]) - 1):
        s1 = sort_string(list(arr[i - 1]))
        s2 = sort_string(list(arr[i]))
        if s1 != s2:
            flag = 0
            break
    else:
        break
if flag == 1:
    print(''.join(arr[0]))
else:
    print('Impossible')
