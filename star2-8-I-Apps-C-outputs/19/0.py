
from collections import deque


def bfs(dictionary, start, end):
    queue = deque([start])
    visited = set([start])
    steps = {start: 0}
    while queue:
        curr = queue.popleft()
        if curr == end:
            return steps[curr]
        for i in range(len(curr)):
            for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                new_word = curr[:i] + c + curr[i + 1:]
                if new_word in dictionary and new_word not in visited:
                    queue.append(new_word)
                    visited.add(new_word)
                    steps[new_word] = steps[curr] + 1
    return -1


def solve(dictionary, start, end):
    n = int(input())
    dictionary = set(input() for _ in range(n))
    if end not in dictionary:
        return 0, -1
    min_steps = n + 1
    min_word = None
    for i in range(len(start)):
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new_word = start[:i] + c + start[i + 1:]
            if new_word not in dictionary:
                continue
            dictionary.add(new_word)
            steps = bfs(dictionary, new_word, end)
            dictionary.remove(new_word)
            if steps != -1 and steps < min_steps:
                min_steps = steps
                min_word = new_word
    return min_word, min_steps


if __name__ == '__main__':
    start, end = input(), input()
    word, steps = solve(set(), start, end)
    print(word)
    print(steps)


