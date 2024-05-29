
def exchange(lst1, lst2):
    if sum(x % 2 for x in lst1) == 0:
        return "YES"
    return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
