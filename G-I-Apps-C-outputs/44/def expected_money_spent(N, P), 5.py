
def expected_money_spent(N, P):
    money_spent = 0
    prob_fail = 1 - P
    prob_success = P
    total_cost = 0
    
    for _ in range(N):
        while True:
            total_cost += 5
            money_spent += 5
            if random.random() < prob_success:
                break
                
    expected_cost = money_spent / N
    return expected_cost

N, P = map(float, input().split())

result = expected_money_spent(N, P)
print("{:.9f}".format(result))
