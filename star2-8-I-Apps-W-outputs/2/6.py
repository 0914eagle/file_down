
def cbs(n, m, p, s, op):
    s = list(s)
    def find_pair(pos):
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack[-1] == pos:
                    return i
                stack.pop()
    for o in op:
        if o == "L" and p > 1:
            p -= 1
        elif o == "R" and p < n:
            p += 1
        elif o == "D":
            pair = find_pair(p - 1)
            s[p - 1] = ""
            s[pair] = ""
            for i in range(p, pair + 1):
                s[i] = ""
            p = max(1, p - 1)
    return "".join(s)

n, m, p = map(int, input().split())
s = input()
op = input()
print(cbs(n, m, p, s, op))

