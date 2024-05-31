
def frequency_sorter(message_length, max_number, message):
    counts = {}
    
    for num in message:
        counts[num] = counts.get(num, 0) + 1
    
    sorted_message = sorted(message, key=lambda x: (-counts[x], message.index(x)))
    
    return sorted_message

# Read input
input_line = input().strip().split()
N, C = map(int, input_line)
message = list(map(int, input().strip().split()))

# Call the function and print the result
sorted_sequence = frequency_sorter(N, C, message)
print(" ".join(map(str, sorted_sequence)))
