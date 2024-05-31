uency_sorter(N, C, message):
    frequencies = {}
    for num in message:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    
    sorted_message = sorted(message, key=lambda x: (-frequencies[x], message.index(x)))
    return sorted_message

# Input processing
N, C = map(int, input().split())
message = list(map(int, input().split()))

sorted_sequence = frequency_sorter(N, C, message)
print(*sorted_sequence