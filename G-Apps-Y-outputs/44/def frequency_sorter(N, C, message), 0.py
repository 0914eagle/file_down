
def frequency_sorter(N, C, message):
    frequency = {}
    for num in message:
        frequency[num] = frequency.get(num, 0) + 1
    
    sorted_message = sorted(message, key=lambda x: (-frequency[x], message.index(x)))
    
    return sorted_message

# Read input
N, C = map(int, input().split())
message = list(map(int, input().split()))

# Call the frequency_sorter function and print the sorted sequence
sorted_sequence = frequency_sorter(N, C, message)
print(*sorted_sequence)
