
def frequency_sorter(N, C, message):
    freq_count = {}
    for num in message:
        if num in freq_count:
            freq_count[num] += 1
        else:
            freq_count[num] = 1
    
    sorted_message = sorted(message, key=lambda x: (-freq_count[x], message.index(x)))
    return sorted_message

# Input processing
N, C = map(int, input().split())
message = list(map(int, input().split()))

# Call the function and print the output
sorted_sequence = frequency_sorter(N, C, message)
print(*sorted_sequence)
