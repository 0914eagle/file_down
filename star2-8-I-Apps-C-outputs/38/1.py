
def solve(s):
    stack = []
    notation = ""
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append((i, ch))
        elif ch == ")":
            start, ch = stack.pop()
            end = i + 1
            notation += str(start) + "," + str(end) + ":"
    print(notation)

if __name__ == "__main__":
    s = input()
    solve(s)

