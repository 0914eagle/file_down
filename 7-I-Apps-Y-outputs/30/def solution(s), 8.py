
def solution(s):
    # your code here
    n = len(s)
    if n % 3 == 0:
        return s
    if n % 3 == 1:
        if s[0] == '0':
            return '0' + s[1:]
        if s[0] == '1':
            return '2' + s[1:]
        if s[0] == '2':
            return '1' + s[1:]
    if n % 3 == 2:
        if s[0] == '0':
            return '2' + s[1:]
        if s[0] == '1':
            return '0' + s[1:]
        if s[0] == '2':
            return '1' + s[1:]


