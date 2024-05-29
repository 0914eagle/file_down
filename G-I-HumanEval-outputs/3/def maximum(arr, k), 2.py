
def maximum(arr, k):
    if k > len(arr):
        return sorted(arr, reverse=True)

    return sorted(arr, reverse=True)[:k]
