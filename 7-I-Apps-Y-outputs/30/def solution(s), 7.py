
def solution(s):
    n = len(s)
    if n % 3 != 0:
        return -1
    if s == s[::-1]:
        return s
    if s.count('0') == s.count('1') and s.count('1') == s.count('2'):
        return s
    if s.count('0') == s.count('1') and s.count('1') != s.count('2'):
        return s.replace('0', '2').replace('1', '0').replace('2', '1')
    if s.count('0') != s.count('1') and s.count('1') == s.count('2'):
        return s.replace('0', '1').replace('1', '2').replace('2', '0')
    if s.count('0') != s.count('1') and s.count('1') != s.count('2'):
        return s.replace('0', '2').replace('1', '0').replace('2', '1')

