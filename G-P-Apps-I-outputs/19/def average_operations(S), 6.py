
def average_operations(S):
    count_H = S.count('H')
    count_T = S.count('T')
    count_question = S.count('?')

    total_possibilities = 2 ** count_question

    total_operations = 0
    for i in range(total_possibilities):
        current_H = count_H
        current_T = count_T
        current_operations = 0

        for j in range(count_question):
            if (i >> j) & 1 == 1:
                current_H += 1
            else:
                current_T += 1

            if current_H > 0:
                current_H -= 1
                current_operations += 1
            else:
                break

        total_operations += current_operations

    return total_operations / total_possibilities

# Input
S = input().strip()

# Output
result = average_operations(S)
print(result)
```
