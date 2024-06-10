
import re

def get_vars(program):
    var_map = {'?': '0', '_': '1', '-': '2', '+': '3', '*': '4', '/': '5', ':': '6', '>': '7', '<': '8', '.': '9'}
    return re.sub(r'[^?_+-*/:<>.,]', '', program).translate(var_map)

def find_feed(program, jaws, stomach):
    if len(program) == 0:
        return ''.join(stomach)
    if program[0] in '0123456789':
        stomach.append(program[0])
        return find_feed(program[1:], jaws, stomach)
    if program[0] in '<>':
        if program[0] == '>':
            jaws.append(stomach.pop(0))
        else:
            stomach.insert(0, jaws.pop())
        return find_feed(program[1:], jaws, stomach)
    if program[0] == '.':
        return find_feed(program[1:], jaws, stomach)
    if program[0] in '+-*/':
        if len(stomach) < 2:
            return False
        v1 = stomach.pop()
        v2 = stomach.pop()
        result = str(eval(v2 + program[0] + v1))
        stomach.append(result)
        return find_feed(program[1:], jaws, stomach)
    return False


program = input()
vars = get_vars(program)

for i in range(10000):
    feed = str(i).zfill(len(vars))
    result = find_feed(program, [], list(feed))
    if result:
        print(result)
        break
else:
    print("false")

