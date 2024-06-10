
import re
from itertools import permutations
from typing import List, Tuple


def solve_rebus(rebus: str) -> Tuple[str, List[int]]:
    
    numbers, operators, total = re.split(r'([\+\-=])', rebus.strip()), [], 0
    for i, number in enumerate(numbers):
        if number == '?':
            operators.append(i)
        else:
            total += int(number)
    for replacements in permutations(range(1, total + 1), len(operators)):
        equation = rebus
        for i, index in enumerate(operators):
            equation = equation.replace('?', str(replacements[i]), 1)
        if eval(equation):
            return equation, list(replacements)
    return None, None


if __name__ == '__main__':
    rebus = input().strip()
    solution, replacements = solve_rebus(rebus)
    if solution:
        print('Possible')
        print(solution)
    else:
        print('Impossible')

