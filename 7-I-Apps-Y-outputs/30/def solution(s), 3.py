
def solution(s):
    # your code here
    n = len(s)
    if n % 3 == 0:
        return s
    if n % 3 == 1:
        return s[:n//3] + '0' + s[n//3:]
    if n % 3 == 2:
        return s[:n//3] + '2' + s[n//3:]

