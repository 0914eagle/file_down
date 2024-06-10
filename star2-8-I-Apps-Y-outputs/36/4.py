
from sys import stdin
input = stdin.readline

k = int(input())

even = k // 2
odd = k - even

print(even * odd)

