
def find_cafe(arr):
    last_seen = dict()
    max_interval = 0
    cafe_idx = 0
    for idx, val in enumerate(arr):
        if val not in last_seen:
            last_seen[val] = idx
        else:
            interval = idx - last_seen[val]
            if interval > max_interval:
                max_interval = interval
                cafe_idx = val

    return cafe_idx


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_cafe(arr))

