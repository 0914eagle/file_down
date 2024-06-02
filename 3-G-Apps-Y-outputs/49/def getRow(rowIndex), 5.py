
def getRow(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    return row

# Test the function with an example
print(getRow(3))  # Output: [1, 3, 3, 1]
