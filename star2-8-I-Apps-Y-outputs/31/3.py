
from sys import stdin

def palindrome(arr):
    if len(arr) < 3:
        return False
    return arr == arr[::-1]

def subsequence(arr):
    for i in range(len(arr)-2):
        if palindrome(arr[i:i+3]):
            return True
    return False

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    if subsequence(arr):
        print("YES")
    else:
        print("NO")

