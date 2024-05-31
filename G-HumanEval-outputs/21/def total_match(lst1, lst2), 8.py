
def total_match(lst1, lst2):
    len_lst1 = sum(len(word) for word in lst1)
    len_lst2 = sum(len(word) for word in lst2)

    if len_lst1 < len_lst2:
        return lst1
    elif len_lst1 > len_lst2:
        return lst2
    else:
        return lst1

# Test cases
print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']
