
def solve(s, t):
    if s == t:
        return "Yes"
    for _ in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            return "Yes"
    return "No"

if __name__ == "__main__":
    s = input()
    t = input()
    print(solve(s, t))

