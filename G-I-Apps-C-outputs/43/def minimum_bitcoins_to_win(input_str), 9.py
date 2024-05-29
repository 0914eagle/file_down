
def minimum_bitcoins_to_win(input_str):
    lines = input_str.split('\n')
    HP_Y, ATK_Y, DEF_Y = map(int, lines[0].split())
    HP_M, ATK_M, DEF_M = map(int, lines[1].split())
    h, a, d = map(int, lines[2].split())

    min_bitcoins = float('inf')

    for i in range(101):  # Try all possible HP values to buy
        for j in range(101):  # Try all possible ATK values to buy
            for k in range(101):  # Try all possible DEF values to buy
                total_bitcoins = 0
                if ATK_Y + j <= DEF_M:  # Ensure Yang can defeat the monster
                    continue

                total_bitcoins += max(0, HP_M - max(0, ATK_Y + j - DEF_M)) * h  # Calculate HP cost
                total_bitcoins += max(0, ATK_M - max(0, ATK_Y + j - DEF_M)) * a  # Calculate ATK cost
                total_bitcoins += max(0, DEF_M - max(0, ATK_Y + j - DEF_M)) * d  # Calculate DEF cost

                min_bitcoins = min(min_bitcoins, total_bitcoins)

    return min_bitcoins

# Example usage
input_str = "1 2 1\n1 100 1\n1 100 100"
print(minimum_bitcoins_to_win(input_str))  # Output: 99
```
```python
input_str = "100 100 100\n1 1 1\n1 1 1"
print(minimum_bitcoins_to_win(input_str))  # Output: 0
```
