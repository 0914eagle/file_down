
def fruit_distribution(s, n):
    # Split the input string to get the numbers of apples and oranges
    fruits_list = s.split(" and ")
    apples = int(fruits_list[0].split()[0])
    oranges = int(fruits_list[1].split()[0])
    
    # Calculate the number of mango fruits in the basket
    mango = n - apples - oranges
    
    return mango
```
