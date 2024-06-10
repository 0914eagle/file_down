
from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    quarrels = set([tuple(map(int, input().split())) for _ in range(k)])
    graph = [[] for _ in range(n)]
    for i, skill_i in enumerate(skills):
        for j, skill_j in enumerate(skills):
            if skill_i > skill_j and (i+1, j+1) not in quarrels:
                graph[i].append(j)
    answer = [0] * n
    stack = [i for i in range(n)]
    while stack:
        cur = stack.pop()
        for neighbor in graph[cur]:
            answer[neighbor] += 1
            stack.append(neighbor)
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()

