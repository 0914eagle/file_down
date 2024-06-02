
def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Count the number of odd elements in lst2
    odd_count += sum(1 for num in lst2 if num % 2 != 0)
    
    # If the total number of odd elements is even, it is possible to exchange elements to make lst1 all even
    if odd_count % 2 == 0:
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
