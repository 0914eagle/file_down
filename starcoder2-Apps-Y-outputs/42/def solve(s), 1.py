
def solve(s):
    return "Yes" if s == "abc" or s == "acb" or s == "bac" or s == "bca" or s == "cab" or s == "cba" else "No"

if __name__ == "__main__":
    s = input()
    print(solve(s))

