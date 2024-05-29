
def exchange(lst1, lst2):
    # Count number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Count number of odd elements in lst2
    odd_count2 = sum(1 for num in lst2 if num % 2 != 0)
    
    # If there are enough odd elements in lst2 to replace the odd elements in lst1, return "YES"
    if odd_count <= len(lst2) - odd_count2:
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Should return "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Should return "NO"
