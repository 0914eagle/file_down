
def rearrange_line(n, dollars):
    dollars.sort()
    for i in range(n):
        if dollars[i] < i:
            return ":("
    result = [0] * n
    for i in range(n):
        result[(i + dollars[i]) % n] = dollars[i]
    return ' '.join(map(str, result))

# Input
n = int(input())
dollars = list(map(int, input().split()))

# Output
print(rearrange_line(n, dollars))
