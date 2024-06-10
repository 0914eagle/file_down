
import sys


def main():
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
        sorted_arr = sorted(arr[:3])
        print(sorted_arr[len(sorted_arr) // 2])
    elif t == 4:
        print(sum(arr))
    elif t == 5:
        print(sum(num for num in arr if num % 2 == 0))
    elif t == 6:
        print("".join(chr(ord("a") + num % 26) for num in arr))
    elif t == 7:
        curr_idx = 0
        while 0 <= curr_idx < n - 1:
            curr_idx = arr[curr_idx]
        if curr_idx == n - 1:
            print("Done")
        elif curr_idx < 0 or curr_idx >= n:
            print("Out")
        else:
            print("Cyclic")


if __name__ == "__main__":
    main()


