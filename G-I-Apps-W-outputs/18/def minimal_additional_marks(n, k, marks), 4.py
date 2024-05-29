
def minimal_additional_marks(n, k, marks):
    average_mark = sum(marks) / n
    additional_marks = 0

    while average_mark < k - 0.5:
        additional_marks += 1
        marks.append(k)
        n += 1
        average_mark = sum(marks) / n

    return additional_marks

# Reading input
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Calling the function and printing the result
print(minimal_additional_marks(n, k, marks))
```
