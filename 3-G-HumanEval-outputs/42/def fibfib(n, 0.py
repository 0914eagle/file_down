
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_list = [0, 0, 1]
        for i in range(3, n+1):
            fibfib_list.append(fibfib_list[i-1] + fibfib_list[i-2] + fibfib_list[i-3])
        return fibfib_list[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
