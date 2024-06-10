
import sys


def main():
    num_words = int(input())
    dictionary = set()
    for _ in range(num_words):
        dictionary.add(input().strip())
    start, end = input().strip(), input().strip()
    visited = set()
    queue = [(start, 0)]
    while queue:
        word, steps = queue.pop(0)
        if word == end:
            print(word)
            print(steps)
            return
        if word in visited:
            continue
        visited.add(word)
        for i in range(len(word)):
            for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                new_word = word[:i] + c + word[i + 1:]
                if new_word in dictionary:
                    queue.append((new_word, steps + 1))
    print(0)
    print(-1)


if __name__ == "__main__":
    main()

