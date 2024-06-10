
def solve(a, b):
    res = 0
    for i in range(a, b+1):
        res += count_number_of_occurrences(i)
    
    return res

def count_number_of_occurrences(num):
    res = 1
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    
    res += count_number_of_occurrences(rev)
    
    return res

q = int(input())

for i in range(q):
    a, b = map(int, input().split())
    
    print(solve(a, b))

