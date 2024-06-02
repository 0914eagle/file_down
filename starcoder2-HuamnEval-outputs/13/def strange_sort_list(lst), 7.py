
def strange_sort_list(lst):
    if lst == []:
        return []
    else:
        return sorted(lst)[::2] + sorted(lst)[::-2]
 