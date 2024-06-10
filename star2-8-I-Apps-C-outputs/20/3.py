
#!/usr/bin/env python
import re


def solve(rebus):
    left_side, right_side = rebus.split("=")
    left_side = left_side.split(" ")
    right_side = int(right_side)
    left_sum = 0
    left_pos = []
    for idx, val in enumerate(left_side):
        if val == "?":
            left_pos.append(idx)
        else:
            left_sum += int(val)
    left_sum = right_side - left_sum
    if left_sum <= 0:
        return "Impossible"
    else:
        answer = left_side[:]
        for idx in left_pos:
            answer[idx] = str(left_sum)
        return " ".join(answer) + " = " + str(right_side)


if __name__ == "__main__":
    rebus = raw_input()
    pattern = r"^\?([\+-]\?)*=\d+$"
    if re.match(pattern, rebus):
        answer = solve(rebus)
        print answer
    else:
        print "Input is not a valid rebus"


