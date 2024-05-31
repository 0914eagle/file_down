
def frequency_sorter(N, C, message):
    freq_map = {}
    for num in message:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    sorted_message = sorted(message, key=lambda x: (-freq_map[x], message.index(x)))
    return sorted_message

# Input parsing
N, C = map(int, input().split())
message = list(map(int, input().split()))

sorted_sequence = frequency_sorter(N, C, message)
print(*sorted_sequence)
