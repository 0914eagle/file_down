
import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

def make_coprime_array(n, arr):
    k = 0
    new_arr = [arr[0]]
    
    for i in range(1, n):
        if not is_coprime(new_arr[-1], arr[i]):
            k += 1
            new_arr.append(1)
        new_arr.append(arr[i])
    
    return k, new_arr

# Input
n = int(input())
arr = list(map(int, input().split()))

# Solve and output
k, new_arr = make_coprime_array(n, arr)
print(k)
print(*new_arr)
