
def solve_rebus(rebus):
    left_sum, right_sum, n = 0, 0, 0
    is_left = True
    is_question = False
    for c in rebus:
        if c.isdigit():
            if is_question:
                if is_left:
                    left_sum = left_sum * 10 + int(c)
                else:
                    right_sum = right_sum * 10 + int(c)
            else:
                n = n * 10 + int(c)
        elif c == '+':
            is_left = True
        elif c == '-':
            is_left = False
        elif c == '?':
            is_question = True
        else:
            is_question = False
    if left_sum + right_sum != n:
        return "Impossible"
    left_nums = [1]
    right_nums = [n]
    for i in range(1, len(rebus) - 1):
        if rebus[i] == '+':
            right_nums[-1] -= left_nums[-1]
            left_nums.append(1)
            right_nums.append(right_nums[-1])
        elif rebus[i] == '-':
            left_nums[-1] -= right_nums[-1]
            right_nums.append(1)
            left_nums.append(left_nums[-1])
    result = ""
    for i in range(len(rebus)):
        if rebus[i] == '?':
            result += str(left_nums.pop(0))
        else:
            result += rebus[i]
    return result

