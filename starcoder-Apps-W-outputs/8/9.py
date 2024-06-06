

def main():
    # Get the size of array
    n, m, k = list(map(int, input().split()))

    # Get the array
    a = list(map(int, input().split()))

    # Get the minimum
    a.sort(reverse=True)

    # Initialize the array of indices
    indices = [m] * (k - 1)

    # Calculate the answer
    ans = 0
    for i in range(0, k - 1):
        ans += sum(a[i * m:(i + 1) * m])

    # Print the answer
    print(ans)
    print(*indices)

if __name__ == "__main__":
    main()
