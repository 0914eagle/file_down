
import sys

def add_word(start, end, words):
    '''
    start: str, the start of the word ladder
    end: str, the end of the word ladder
    words: set, a set of words in the dictionary
    '''
    length = len(start)
    queue = [(start, 0)]
    visited = set()
    while queue:
        curr, step = queue.pop(0)
        if curr == end:
            return step
        for i in range(length):
            for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                word = curr[:i] + ch + curr[i+1:]
                if word in words and word not in visited:
                    queue.append((word, step+1))
                    visited.add(word)
    return -1

def main():
    '''
    main function
    '''
    n = int(input())
    words = set()
    for _ in range(n):
        word = input()
        words.add(word)
    start = input()
    end = input()
    min_steps = add_word(start, end, words)
    print(min_steps)

if __name__ == '__main__':
    main()


