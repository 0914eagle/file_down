
'''
import sys
input = sys.stdin.readline

def solve(n, q, salary, height, boss, subordinate):
    boss = [None] * n
    subordinate = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if salary[i] > salary[j] and height[i] >= height[j]:
                boss[i] = j
                subordinate[j].append(i)
    for i in q:
        print(boss[i], len(subordinate[i]))

if __name__ == "__main__":
    n, q = map(int, input().split())
    salary = [0] * n
    height = [0] * n
    for i in range(n):
        id, salary[i], height[i] = map(int, input().split())
    q = [int(input()) for _ in range(q)]
    solve(n, q, salary, height, boss, subordinate)

