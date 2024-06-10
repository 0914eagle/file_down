
from collections import Counter

def is_palindrome(arr):
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            return False
    return True

def solve(arr):
    n = len(arr)
    counter = Counter(arr)
    for k, v in counter.items():
        if v >= 2:
            return True
    
    for i in range(n - 2):
        for j in range(i + 2, n):
            if arr[i] == arr[j]:
                subarr = arr[i+1:j]
                if is_palindrome(subarr):
                    return True
    
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if solve(arr):
        print("YES")
    else:
        print("NO")

