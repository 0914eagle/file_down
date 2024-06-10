
import sys

def wordLadder(dictionary, start, end):
    length = len(start)
    queue = [start]
    visited = {start}
    depth = 0
    while queue:
        newQueue = []
        for word in queue:
            if word == end:
                return depth
            for i in range(length):
                for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in dictionary and newWord not in visited:
                        visited.add(newWord)
                        newQueue.append(newWord)
        queue = newQueue
        depth += 1
    return -1

def main():
    dictionary = set()
    n = int(sys.stdin.readline())
    for _ in range(n):
        dictionary.add(sys.stdin.readline().strip())
    start, end = sys.stdin.readline().split()
    minSteps = wordLadder(dictionary, start, end)
    if minSteps == -1:
        print(0)
        print(-1)
    else:
        for word in sorted(dictionary):
            newDictionary = dictionary.copy()
            newDictionary.add(word)
            steps = wordLadder(newDictionary, start, end)
            if steps == minSteps:
                print(word)
                print(minSteps)
                return

main()

