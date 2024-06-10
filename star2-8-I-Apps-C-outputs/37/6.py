
def solve_problem(d, b, f, t_0, t_1, t_2):
    
    
    best_bling = b
    
    # We can keep track of the current state of Johan's fruit farm
    # using the following variables:
    current_fruits = f
    current_bling = b
    current_fruit_trees = [t_0, t_1, t_2]
    
    for day in range(d):
        best_bling = max(best_bling, current_bling + current_fruits * 100)
        
        new_fruits = current_fruit_trees[0]
        new_bling = new_fruits * 100
        
        current_fruit_trees = [current_fruit_trees[1], current_fruit_trees[2], 0]
        
        if day >= 2:
            current_fruit_trees[0] += 3
        
        current_fruits += new_fruits
        current_bling += new_bling
    
    return best_bling
    

