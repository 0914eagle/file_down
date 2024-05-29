
def exchange(lst1, lst2):
    even_count = sum(1 for num in lst1 if num % 2 == 0)
    # Count the number of even numbers in lst1

    total_count = len(lst1) + len(lst2)
    # Total number of elements in lst1 and lst2

    return "YES" if even_count % 2 == 0 or (total_count - even_count) % 2 == 0 else "NO"
    # The condition to be able to exchange elements to make lst1 only even is that either lst1 has even count of evens
    # or the remaining elements in lst1 and all elements of lst2 can be swapped to make it even
```
