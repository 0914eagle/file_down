
def frequency_sorter(N, C, message):
    freq = {}
    for num in message:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    sorted_message = sorted(message, key=lambda x: (-freq[x], message.index(x)))

    return sorted_message

# Reading input
N, C = map(int, input().split())
message = list(map(int, input().split()))

# Calling the function and printing the output
sorted_sequence = frequency_sorter(N, C, message)
print(*sorted_sequence)
