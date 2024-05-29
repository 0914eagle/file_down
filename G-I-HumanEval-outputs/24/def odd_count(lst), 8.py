
def odd_count(lst):
    
    result = []
    for string in lst:
        count = sum(1 for digit in string if int(digit) % 2 != 0)
        formatted_string = f"the number of odd elements {count}n the str{count}ng {string} of the {string}nput."
        result.append(formatted_string)
    return result
```
