
 def strange_sort_list(lst):
    if not lst:
        return lst
    else:
        return sorted(lst, key=lambda x: (x % 2, -x))
 