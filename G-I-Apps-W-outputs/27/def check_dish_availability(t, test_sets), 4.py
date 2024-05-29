
def check_dish_availability(t, test_sets):
    for _ in range(t):
        m, k = map(int, test_sets[_][0].split())
        dish_count = list(map(int, test_sets[_][1].split()))
        
        remaining_dishes = dish_count[:]
        for i in range(m-1):
            t_j, r_j = map(int, test_sets[_][i+2].split())
            if t_j != 0 and r_j == 0:
                remaining_dishes[t_j-1] -= 1
        
        result = ""
        for count in remaining_dishes:
            if count >= m:
                result += "N"
            else:
                result += "Y"
        
        print(result)

test_sets = [
    ["3 4", "2 3 2 1", "1 0", "0 0"],
    ["5 5", "1 2 1 3 1", "3 0", "0 0", "2 1", "4 0"]
]
check_dish_availability(2, test_sets)
```
