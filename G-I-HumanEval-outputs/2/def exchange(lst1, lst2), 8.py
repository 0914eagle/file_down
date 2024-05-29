
def exchange(lst1, lst2):
    if sum(x % 2 != 0 for x in lst1) > sum(x % 2 != 0 for x in lst2):
        return "NO"
    return "YES"

# Test Cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
```
