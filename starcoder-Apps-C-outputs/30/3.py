
from collections import defaultdict
from copy import deepcopy
import re

def solve(s, words):
    graph = defaultdict(set)
    s = re.sub(" ", "", s)

    for word in words:
        if len(s) != len(word):
            continue
        for i in range(len(s)):
            graph[s[i]].add(word[i])
            graph[word[i]].add(s[i])

    visit = [False] * 26
    parent = [0] * 26
    arr = []

    def dfs(source):
        visit[source] = True

        for n in graph[source]:
            if visit[ord(n) - 97]:
                if n != source:
                    return True
                continue
            if dfs(ord(n) - 97):
                return True
        visit[source] = False
        arr.append(chr(source + 97))
        return False

    for i in range(26):
        if len(graph[chr(i + 97)]) == 0:
            continue

        if dfs(i):
            return "impossible"

    return " ".join(arr[::-1])

def main():
    s = input()
    n = int(input())
    words = [input() for _ in range(n)]

    print(solve(s, words))

main()
