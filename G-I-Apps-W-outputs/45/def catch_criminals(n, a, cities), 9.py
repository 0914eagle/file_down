
def catch_criminals(n, a, cities):
    criminals_caught = 0

    for i in range(n):
        distance = abs(a - (i + 1))
        if cities[i] == 1 and (distance == 0 or cities[a - distance - 1] == 1 or cities[a + distance - 1] == 1):
            criminals_caught += 1

    return criminals_caught

# Taking input
n, a = map(int, input().split())
cities = list(map(int, input().split()))

# Calling the function and printing the output
print(catch_criminals(n, a, cities))
```  
