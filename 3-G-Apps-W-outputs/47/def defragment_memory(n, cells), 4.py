
def defragment_memory(n, cells):
    processes = {}
    operations = 0
    
    for i in range(n):
        if cells[i] != 0:
            if cells[i] not in processes:
                processes[cells[i]] = i
            else:
                operations += i - processes[cells[i]]
                processes[cells[i]] += 1
    
    return operations

# Input
n = int(input())
cells = list(map(int, input().split()))

# Output
print(defragment_memory(n, cells))
