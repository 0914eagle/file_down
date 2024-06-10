
from sys import stdin
from collections import defaultdict

def solve(words, alphabet_size):
    n = len(words)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                continue
            for k in range(min(len(words[i]), len(words[j]))):
                if words[i][k] != words[j][k]:
                    graph[words[i][k]].append(words[j][k])
                    break
            else:
                if len(words[i]) > len(words[j]):
                    return "No"
    capitalized = set()
    for i in range(1, alphabet_size+1):
        if i not in graph:
            continue
        stack = [i]
        while stack:
            cur = stack.pop()
            if cur in capitalized:
                continue
            capitalized.add(cur)
            for nxt in graph[cur]:
                stack.append(nxt)
    return "Yes\n{}\n{}".format(len(capitalized), " ".join(map(str, sorted(capitalized))))

def main():
    n, m = map(int, stdin.readline().split())
    words = []
    for _ in range(n):
        l, *s = map(int, stdin.readline().split())
        words.append(s)
    print(solve(words, m))

if __name__ == "__main__":
    main()

