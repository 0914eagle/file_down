
def rhymes(a, b):
    min_length = min(len(a), len(b))
    for i in range(min_length, max(min_length - 3, 0), -1):
        if a[-i:] == b[-i:]:
            return True
    return False


def solve(statements):
    words = set()
    for statement in statements:
        words.add(statement[0])
        words.add(statement[2])
    for word in words:
        for other_word in words:
            if word != other_word and rhymes(word, other_word):
                if (word, other_word) in statements or (other_word, word) in statements:
                    continue
                return "wait what?"
    return "yes"


if __name__ == "__main__":
    n = int(input())
    statements = []
    for _ in range(n):
        statements.append(input().split(" "))
    print(solve(statements))

