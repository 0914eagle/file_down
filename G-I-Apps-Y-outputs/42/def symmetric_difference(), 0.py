
def symmetric_difference():
    # Input
    M = int(input())
    set_M = set(map(int, input().split()))
    N = int(input())
    set_N = set(map(int, input().split()))

    # Calculate symmetric difference
    sym_diff = sorted(set_M.symmetric_difference(set_N))

    # Output
    for num in sym_diff:
        print(num)

# Call the function to find symmetric difference
symmetric_difference()
