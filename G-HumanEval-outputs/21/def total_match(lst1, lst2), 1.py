
def total_match(lst1, lst2):
    sum_lst1 = sum(len(s) for s in lst1)
    sum_lst2 = sum(len(s) for s in lst2)

    if sum_lst1 < sum_lst2:
        return lst1
    elif sum_lst1 == sum_lst2:
        return lst1
    else:
        return lst2

# Test cases
print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']
