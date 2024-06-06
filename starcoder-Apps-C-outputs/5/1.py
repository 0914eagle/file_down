

def solution(arr):
    sum = arr[0]
    min = arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            min = arr[i]
            if (min > arr[i+1]):
                min = arr[i+1]
        elif (min < arr[i+1]):
            min = arr[i+1]
        sum = sum + min
    return sum


