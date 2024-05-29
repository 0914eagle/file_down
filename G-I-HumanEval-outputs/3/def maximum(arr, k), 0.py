
def maximum(arr, k):
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[:k]
