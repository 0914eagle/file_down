
def find_closest(arr, x, y):
    n = len(arr)
    idx_x = arr.index(x)
    idx_y = arr.index(y)
    clockwise = abs(idx_x - idx_y)
    counter_clockwise = n - clockwise
    return min(clockwise, counter_clockwise)


def guessing_circle(arr):
    n = len(arr)
    unique_numbers = set(arr)
    for x in unique_numbers:
        for y in unique_numbers:
            if x != y:
                if find_closest(arr, x, y) == find_closest(arr, y, x):
                    break
        else:
            continue
        break
    else:
        print(*sorted(unique_numbers), sep="\n")
        return

    print("none")


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    guessing_circle(arr)


