
from itertools import product
from math import factorial

def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def prob(n, m, d):
    healths = [list(map(int, input().split())) for _ in range(2)]
    probs = [[0] * 7 for _ in range(2)]
    probs[0][0] = 1
    probs[1][0] = 1
    for i in range(1, 7):
        probs[0][i] = probs[0][i - 1] * healths[0][i - 1] / 6
        probs[1][i] = probs[1][i - 1] * healths[1][i - 1] / 6
    prob = 0
    for i in range(n + 1):
        prob += nCk(n, i) * probs[0][i] * probs[1][m] * (1 - probs[0][n])**(d - i)
    return prob

n, m, d = map(int, input().split())
print(prob(n, m, d))

