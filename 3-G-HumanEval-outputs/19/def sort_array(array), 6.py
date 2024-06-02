
def sort_array(array):
    sorted_array = array.copy()
    if (array[0] + array[-1]) % 2 == 0:
        sorted_array.sort(reverse=True)
    else:
        sorted_array.sort()
    return sorted_array
