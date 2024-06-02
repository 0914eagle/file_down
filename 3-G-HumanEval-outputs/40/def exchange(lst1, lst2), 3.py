
def exchange(lst1, lst2):
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Calculate the count of odd numbers in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Calculate the count of even numbers in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    
    # If there are enough even numbers in lst2 to replace the odd numbers in lst1
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
