
def defragment_memory(n, cells):
    process_positions = {}
    operations = 0

    for i in range(n):
        if cells[i] != 0:
            if cells[i] not in process_positions:
                process_positions[cells[i]] = i
            else:
                operations += i - process_positions[cells[i]]
                process_positions[cells[i]] += 1

    return operations

# Input processing
n = int(input())
cells = list(map(int, input().split()))

# Call the function and output the result
print(defragment_memory(n, cells))
