
def read_input():
    n = int(input())
    stack = []
    for _ in range(n):
        s = list(input())
        if len(s) > 0:
            stack.append(s)
    return stack, n


def calculate_result(stack, n):
    ans = 0
    for i in range(n):
        for j in range(n):
            s = stack[i][:]
            s.extend(stack[j])
            stack_len = len(s)
            stack_pop = []
            for i in range(stack_len):
                if len(stack_pop) == 0:
                    stack_pop.append(s[i])
                else:
                    if stack_pop[-1] == '(' and s[i] == ')':
                        stack_pop.pop()
                    else:
                        stack_pop.append(s[i])
            if len(stack_pop) == 0:
                ans += 1
    return ans


stack, n = read_input()
print(calculate_result(stack, n))
