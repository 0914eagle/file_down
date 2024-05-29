
def exchange(lst1, lst2):
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    
    total_odd_in_lst1 = sum(1 for x in lst1 if x % 2 == 1)
    total_even_in_lst2 = sum(1 for x in lst2 if x % 2 == 0)
    
    return "YES" if total_odd_in_lst1 <= total_even_in_lst2 else "NO"
