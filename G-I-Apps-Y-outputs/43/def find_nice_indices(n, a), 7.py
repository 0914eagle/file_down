
def find_nice_indices(n, a):
    nice_indices = []
    
    for i in range(n):
        sum_except_i = sum(a) - a[i]
        if a[i] == sum_except_i:
            nice_indices.append(i+1)
    
    k = len(nice_indices)
    
    print(k)
    if k > 0:
        print(" ".join(map(str, nice_indices)))

# Input parsing
n = int(input())
a = list(map(int, input().split()))

# Calling the function
find_nice_indices(n, a)
