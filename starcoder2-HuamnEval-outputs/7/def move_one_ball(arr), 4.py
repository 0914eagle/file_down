
 def move_one_ball(arr):
    if not arr:
        return True
    for i in range(len(arr)):
        if arr[i] < arr[i-1]:
            if i == 1:
                return False
            else:
                if arr[i] < arr[i-2]:
                    return False
    return True
 