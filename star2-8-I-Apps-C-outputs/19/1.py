
def get_word_ladder(words):
    start, end = words[0], words[1]
    dictionary = set(words[2:])
    num_letters = len(start)
    
    added_word = ""
    num_steps = 0
    
    for i in range(num_letters):
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            candidate = start[:i] + letter + start[i+1:]
            if candidate in dictionary:
                continue
            if candidate == end:
                added_word = candidate
                num_steps = 1
                break
            queue = [candidate]
            visited = set([candidate])
            steps = 1
            while queue:
                word = queue.pop(0)
                for j in range(num_letters):
                    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        new_word = word[:j] + char + word[j+1:]
                        if new_word in visited or new_word in dictionary:
                            continue
                        if new_word == end:
                            added_word = new_word
                            num_steps = steps + 1
                            break
                        queue.append(new_word)
                        visited.add(new_word)
                steps += 1
                if added_word:
                    break
        if added_word:
            break
    
    if not added_word:
        num_steps = -1
    
    return added_word, num_steps


if __name__ == "__main__":
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    
    added_word, num_steps = get_word_ladder(words)
    
    print(added_word)
    print(num_steps)

