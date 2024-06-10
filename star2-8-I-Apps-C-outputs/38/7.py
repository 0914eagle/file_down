
def generate_new_string(s):
    stack = []
    pos_map = {}
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            pos = stack.pop()
            pos_map[pos] = i
    new_string = ""
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            pos = stack.pop()
            start = pos + 1
            end = pos_map[pos]
            new_string += str(start) + "," + str(end + 1) + ":"
    return new_string

s = input()
print(generate_new_string(s))

