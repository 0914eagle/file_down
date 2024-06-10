
def solve_rebus(rebus):
    left_sum, right_sum = 0, 0
    left_nums, right_nums = [], []
    is_left = True
    for ch in rebus:
        if ch.isdigit():
            if is_left:
                left_sum += int(ch)
            else:
                right_sum += int(ch)
        elif ch == '+':
            is_left = True
        elif ch == '-':
            is_left = False
        elif ch == '=':
            is_left = False
    if left_sum == right_sum:
        return "Possible"
    else:
        return "Impossible"


rebus = input()
print(solve_rebus(rebus))

