
def exchange(lst1, lst2):
    # Count odd numbers in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Count odd numbers in lst2
    odd_count += sum(1 for num in lst2 if num % 2 != 0)
    
    return "YES" if odd_count % 2 == 0 else "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Should return "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Should return "NO"
