
def balanced_ternary(s):
    n = len(s)
    if n % 3 == 0:
        return s
    else:
        if s.count('0') > s.count('1'):
            s = s.replace('0', '2')
            s = s.replace('1', '0')
            s = s.replace('2', '1')
        else:
            s = s.replace('1', '2')
            s = s.replace('2', '0')
            s = s.replace('0', '1')
        return s


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(balanced_ternary(s))

