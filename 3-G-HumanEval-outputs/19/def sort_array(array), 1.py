
def sort_array(array):
    sorted_array = array.copy()
    if (sorted_array and (sorted_array[0] + sorted_array[-1]) % 2 == 0) or len(sorted_array) < 2:
        sorted_array.sort(reverse=True)
    else:
        sorted_array.sort()
    return sorted_array
