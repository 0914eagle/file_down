
def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        lst.sort()
        for i in range(len(lst)):
            if lst[i] != lst[i-1]:
                return lst[i]
 