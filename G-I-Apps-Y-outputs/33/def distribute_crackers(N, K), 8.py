
def distribute_crackers(N, K):
    largest = N // K
    remainder = N % K
    smallest = largest
    if remainder != 0:
        largest += 1
        smallest = largest - 1
        remainder -= 1

    return largest - smallest

# Get input values
N, K = map(int, input().split())

# Call the function and print the result
result = distribute_crackers(N, K)
print(result)
```
