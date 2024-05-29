
def maximize_number(n, a, f):
    maximal = list(a)
    for i in range(n):
        digit = int(a[i])
        new_digit = f[digit - 1]
        if new_digit > digit:
            maximal[i] = str(new_digit)
            break
    return ''.join(maximal)

# Read input
n = int(input())
a = input()
f = list(map(int, input().split()))

# Call the function and print the result
print(maximize_number(n, a, f))
