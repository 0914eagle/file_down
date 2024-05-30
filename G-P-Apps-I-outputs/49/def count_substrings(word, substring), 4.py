
def count_substrings(word, substring):
    count = 0
    for i in range(len(word) - len(substring) + 1):
        if word[i:i + len(substring)] == substring:
            count += 1
    return count

def solve_barbarians_game():
    N = int(input())
    barbarians = [input().strip() for _ in range(N)]

    Q = int(input())
    words_shown = []
    answers = []

    for _ in range(Q):
        T, *args = input().strip().split()
        if T == '1':
            words_shown.append(args[0])
        elif T == '2':
            S = int(args[0])
            word = barbarians[S - 1]
            total_count = 0
            for w in words_shown:
                total_count += count_substrings(w, word)
            answers.append(total_count)

    for ans in answers:
        print(ans)

solve_barbarians_game()
```
