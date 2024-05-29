
def smallest_change(arr):
    def is_palindromic(ls):
        return ls == ls[::-1]

    def changes_to_palindrome(ls):
        changes = 0
        for i in range(len(ls) // 2):
            if ls[i] != ls[-(i + 1)]:
                changes += 1
        return changes

    return changes_to_palindrome(arr)

# Test cases
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))  # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # 1
print(smallest_change([1, 2, 3, 2, 1]))  # 0
```
