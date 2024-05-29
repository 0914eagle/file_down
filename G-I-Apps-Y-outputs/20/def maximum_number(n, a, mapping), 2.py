
def maximum_number(n, a, mapping):
    digits = list(map(int, a))
    converted_digits = [mapping[d] for d in digits]
    max_number = int(''.join(map(str, converted_digits)))

    for i in range(n):
        original_digit = digits[i]
        converted_digit = mapping[original_digit]
        
        if converted_digit > original_digit:
            converted_digits[i] = converted_digit
            number = int(''.join(map(str, converted_digits)))
            max_number = max(max_number, number)
            converted_digits[i] = original_digit
    
    return max_number

n = int(input())
a = input().strip()
mapping = list(map(int, input().split()))

result = maximum_number(n, a, mapping)
print(result)
```
