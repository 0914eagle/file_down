
def solve_game(N, barbarians, Q, rounds):
    # Create a dictionary to store the occurrences of each word shown by Tarzan
    word_occurrences = {}
    for i in range(1, N+1):
        word_occurrences[barbarians[i-1]] = 0
    
    result = []
    
    for round_type, arg in rounds:
        if round_type == 1:
            word = arg
            for i in range(1, N+1):
                if barbarians[i-1] in word:
                    word_occurrences[barbarians[i-1]] += 1
        elif round_type == 2:
            barbarian_index = arg
            result.append(word_occurrences[barbarians[barbarian_index-1]])

    return result

# Input parsing
N = int(input())
barbarians = [input() for _ in range(N)]
Q = int(input())
rounds = []
for _ in range(Q):
    round_type, *args = input().split()
    if round_type == '1':
        rounds.append((1, args[0]))
    elif round_type == '2':
        rounds.append((2, int(args[0])))

# Call the function and print the results
answers = solve_game(N, barbarians, Q, rounds)
for ans in answers:
    print(ans)
```
