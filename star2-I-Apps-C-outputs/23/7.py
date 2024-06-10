
from itertools import permutations

def solve(n, pairs):
    operators = ['+', '-', '*']
    for pair in pairs:
        for op in operators:
            if eval(f'{pair[0]}{op}{pair[1]}') not in results:
                results.append(eval(f'{pair[0]}{op}{pair[1]}'))
                break
        else:
            return 'impossible'
    return '\n'.join([f'{pair[0]} {op} {pair[1]} = {results[i]}' for i, (pair, op) in enumerate(zip(pairs, operators))])

n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]
results = []
print(solve(n, pairs))

