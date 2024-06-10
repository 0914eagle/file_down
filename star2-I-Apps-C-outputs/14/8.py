
def rhyme(word1, word2):
    min_length = min(len(word1), len(word2))
    for i in range(min_length, max(min_length - 3, 0), -1):
        if word1[-i:] == word2[-i:]:
            return True
    return False


def check_consistency(statements):
    words = set()
    for statement in statements:
        words.add(statement[0])
        words.add(statement[2])
    for word1 in words:
        for word2 in words:
            if word1 != word2:
                if rhyme(word1, word2):
                    for statement in statements:
                        if (statement[0] == word1 and statement[2] == word2) or (statement[0] == word2 and statement[2] == word1):
                            return "wait what?"
    return "yes"


n = int(input())
statements = []
for _ in range(n):
    statement = input().split()
    statements.append(statement)

print(check_consistency(statements))

