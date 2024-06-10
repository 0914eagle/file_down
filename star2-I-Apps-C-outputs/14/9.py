
def solve(statements):
    graph = {}
    for statement in statements:
        if "is" in statement:
            word1, word2 = statement.split(" is ")
            if word1 not in graph:
                graph[word1] = set()
            if word2 not in graph:
                graph[word2] = set()
            graph[word1].add(word2)
            graph[word2].add(word1)
        else:
            word1, word2 = statement.split(" not ")
            if word1 not in graph:
                graph[word1] = set()
            if word2 not in graph:
                graph[word2] = set()
            graph[word1].add(word2)
            graph[word2].add(word1)
    for word in graph:
        for other_word in graph:
            if word != other_word and word in graph[other_word]:
                graph[word].add(other_word)
    visited = set()
    def dfs(word):
        visited.add(word)
        for other_word in graph[word]:
            if other_word not in visited:
                dfs(other_word)
    for word in graph:
        if word not in visited:
            dfs(word)
        for other_word in graph:
            if other_word not in visited and other_word in graph[word]:
                return "wait what?"
    return "yes"

n = int(input())
statements = [input() for _ in range(n)]
print(solve(statements))

