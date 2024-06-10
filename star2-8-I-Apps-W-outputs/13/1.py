
def get_median(arr):
    arr.sort()
    mid = (len(arr)-1)//2
    return arr[mid]

def convert_to_character(arr):
    result = ""
    for num in arr:
        char_val = (num % 26) + ord('a')
        result += chr(char_val)
    return result

n, t = map(int, input().split())
arr = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    if arr[0] > arr[1]:
        print("Bigger")
    elif arr[0] == arr[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    print(get_median(arr[:3]))
elif t == 4:
    print(sum(arr))
elif t == 5:
    print(sum([num for num in arr if num % 2 == 0]))
elif t == 6:
    print(convert_to_character(arr))
elif t == 7:
    visited = [False] * n
    current = 0
    while current < n and current >= 0:
        if visited[current]:
            print("Cyclic")
            break
        visited[current] = True
        if current == n-1:
            print("Done")
            break
        current = arr[current]
    else:
        print("Out")

