
def find_numbers(n, k):
    # Check if such representation is possible
    if n % 2 != k % 2 or k > n:
        return "NO"
    
    # Calculate the values for the representation
    values = [1] * k
    total = k
    
    for i in range(k-1):
        diff = total + 2 * values[i] - n
        if diff <= 0:
            values[i] += 2
            total += 2
        else:
            values[i] += diff
            break
    
    return "YES\n" + " ".join(map(str, values))

# Read the number of test cases
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = find_numbers(n, k)
    print(result)
