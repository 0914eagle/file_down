
n = int(input())
p = list(map(int, input().split()))

def swap(i, j):
    p[i], p[j] = p[j], p[i]

def check_sorted():
    for i in range(n-1):
        if p[i] > p[i+1]:
            return False
    
    return True

def find_pos(x):
    for i in range(n):
        if p[i] == x:
            return i
    
    return -1

def move_to_end(i):
    while i < n-1:
        swap(i, i+1)
        i += 1

def move_to_begin(i):
    while i > 0:
        swap(i, i-1)
        i -= 1

def sort_train():
    count = 0
    for i in range(n):
        if p[i] != i+1:
            pos = find_pos(i+1)
            if pos > i:
                move_to_end(pos)
            else:
                move_to_begin(pos)
            count += 1
    
    return count

print(sort_train())

