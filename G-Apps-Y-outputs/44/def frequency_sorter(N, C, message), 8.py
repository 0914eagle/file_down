
def frequency_sorter(N, C, message):
    frequency = {}
    for num in message:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    sorted_message = sorted(message, key=lambda x: (-frequency[x], message.index(x)))

    return ' '.join(map(str, sorted_message))


# Input parsing
N, C = map(int, input().split())
message = list(map(int, input().split()))

# Output
print(frequency_sorter(N, C, message))
