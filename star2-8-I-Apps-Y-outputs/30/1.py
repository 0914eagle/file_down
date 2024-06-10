
def golorp(program):
    stack = []
    output = ""
    memory = [0] * 10
    
    for c in program:
        if c.isdigit():
            stack.append(int(c))
        elif c == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append((a + b) % 10)
        elif c == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append((a - b) % 10)
        elif c == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append((a * b) % 10)
        elif c == '/':
            a = stack.pop()
            b = stack.pop()
            if b == 0:
                stack.append(0)
            else:
                stack.append((a // b) % 10)
        elif c == ':':
            stack.append(memory[stack.pop()])
        elif c == '.':
            output += str(stack.pop())
        elif c == ',':
            memory[stack.pop()] = stack.pop()
            
    return output
    
def golorp_problem(program):
    values = golorp(program)
    if len(values) == 0:
        return "false"
    else:
        return values

