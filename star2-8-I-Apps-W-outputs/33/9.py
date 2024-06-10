
from itertools import product

s1 = input()
s2 = input()

def process_command(c):
    if c == '+':
        return 1
    elif c == '-':
        return -1
    else:
        return 0

pos_s1 = sum(map(process_command, s1))
pos_s2 = sum(map(process_command, s2))

if pos_s1 != pos_s2:
    print(0)
else:
    num_choices = s2.count('?')
    prob_choices = [0.5] * num_choices
    probs = [p for p in product([1, -1], repeat=num_choices)]
    count = 0
    for p in probs:
        pos_s2_new = pos_s2
        for i in range(num_choices):
            pos_s2_new += p[i]
        if pos_s2_new == pos_s1:
            count += 1

    print(count / len(probs))

