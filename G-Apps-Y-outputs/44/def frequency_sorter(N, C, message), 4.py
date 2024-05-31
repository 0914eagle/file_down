
def frequency_sorter(N, C, message):
    freq_count = {}
    for num in message:
        if num not in freq_count:
            freq_count[num] = 1
        else:
            freq_count[num] += 1

    sorted_message = sorted(message, key=lambda x: (-freq_count[x], message.index(x)))
    return sorted_message

# Read input
N, C = map(int, input().split())
message = list(map(int, input().split()))

# Call the function and print the result
sorted_sequence = frequency_sorter(N, C, message)
print(' '.join(map(str, sorted_sequence)))
