
def smallest_columns_to_delete(N, row1, row2, row3):
    count = 0
    for i in range(N):
        if sorted([row1[i], row2[i], row3[i]]) != [row1[i], row2[i], row3[i]]:
            count += 1
    return count

# Read input
N = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

# Call the function and output the result
result = smallest_columns_to_delete(N, row1, row2, row3)
print(result)
