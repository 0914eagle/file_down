
def make_sequence_correct(n, seq):
    opens = 0
    need_close = 0
    nanoseconds = 0

    for i in range(n):
        if seq[i] == '(':
            opens += 1
        else:
            if opens == 0:
                need_close += 1
            else:
                opens -= 1

    if opens == 0 and need_close == 0:
        return 0

    if (opens + need_close) % 2 != 0:
        return -1

    nanoseconds = (opens // 2) + (need_close // 2) + (opens % 2) + (need_close % 2)

    return nanoseconds

# Reading input
n = int(input())
seq = input().strip()

# Calling the function and printing the result
print(make_sequence_correct(n, seq))
