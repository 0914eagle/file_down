
def solve(s, k):
    def count(s, k):
        if k <= len(s):
            return s[k - 1]
        for c in s:
            if c == '1':
                k -= 1
            elif c == '2':
                k -= 2
            elif c == '3':
                k -= 3
            elif c == '4':
                k -= 4
            elif c == '5':
                k -= 5
            elif c == '6':
                k -= 6
            elif c == '7':
                k -= 7
            elif c == '8':
                k -= 8
            elif c == '9':
                k -= 9
            if k <= 0:
                return c
        return None
    res = count(s, k)
    return res

s = input()
k = int(input())
print(solve(s, k))

