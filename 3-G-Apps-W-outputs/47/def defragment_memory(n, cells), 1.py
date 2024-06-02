
def defragment_memory(n, cells):
    process_positions = {}
    operations = 0

    for i in range(n):
        cell = cells[i]
        if cell != 0:
            if cell not in process_positions:
                process_positions[cell] = i
            else:
                operations += i - process_positions[cell]
                process_positions[cell] += 1

    return operations

# Input
n = int(input())
cells = list(map(int, input().split()))

# Output
print(defragment_memory(n, cells))
