
from bisect import bisect_left
from collections import defaultdict

def solve(words, queries):
    result = []
    for query in queries:
        if query[0] == 1:
            word = query[1]
            for word in words:
                bisect_left(words[word], i)
            result.append(1)
        else:
            s = query[1]
            result.append(1)
    return result

def main():
    n = int(input())
    words = defaultdict(list)
    for _ in range(n):
        word = input()
        for i in range(len(word)):
            words[word[i:]].append(i)
    q = int(input())
    queries = []
    for _ in range(q):
        t, *query = map(int, input().split())
        queries.append([t] + query)
    result = solve(words, queries)
    for answer in result:
        print(answer)

if __name__ == '__main__':
    main()

