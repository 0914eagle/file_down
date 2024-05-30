
def is_multiple_of_9(N):
    # Calculate the sum of the digits
    digit_sum = sum(int(d) for d in str(N))
    
    # Check if the sum is a multiple of 9
    if digit_sum % 9 == 0:
        return "Yes"
    else:
        return "No"

N = int(input())
print(is_multiple_of_9(N))
```
