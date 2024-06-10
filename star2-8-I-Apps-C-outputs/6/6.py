
def max_blue_lemonade(child_list):
    lemonade_list = [child[1] for child in child_list]
    if lemonade_list.count('blue') == 0:
        return 0.0
    
    def get_max_rate(lemonade):
        max_rate = 0
        for child in child_list:
            if child[0] == lemonade and child[2] > max_rate:
                max_rate = child[2]
        return max_rate
    
    current_rate = 1
    current_lemonade = 'blue'
    
    while current_lemonade != 'pink':
        current_rate *= get_max_rate(current_lemonade)
        current_lemonade = [child[1] for child in child_list if child[0] == current_lemonade][0]
    
    max_blue_lemonade = 10 / current_rate
    
    if max_blue_lemonade > 10:
        max_blue_lemonade = 10
    
    return max_blue_lemonade

