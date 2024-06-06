
# -*- coding: utf-8 -*-


def balance(s):
    length = len(s)
    i = 0
    while i<length:
        if s[i] == '^':
            break
        i += 1
    s = s[i+1:]
    left = 0
    right = 0
    for i in s:
        if i == '^':
            break
        else:
            left += int(i)
    for i in s[::-1]:
        if i == '^':
            break
        else:
            right += int(i)
    if left == right:
        return 'balance'
    elif left > right:
        return 'left'
    else:
        return 'right'
    
    
if __name__ == '__main__':
    s = input()
    print(balance(s))
    
