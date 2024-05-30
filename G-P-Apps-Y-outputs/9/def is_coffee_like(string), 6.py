
def is_coffee_like(string):
    if len(string) != 6:
        return "No"
    
    if string[2] == string[3] and string[4] == string[5]:
        return "Yes"
    else:
        return "No"

S = input()
print(is_coffee_like(S))
```
