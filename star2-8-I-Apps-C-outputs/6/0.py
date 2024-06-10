
def find_max_blue_lemonade(num_children, exchange_rates):
    pass

if __name__ == "__main__":
    num_children = int(input())
    exchange_rates = []
    for _ in range(num_children):
        offered, wanted, rate = input().split()
        exchange_rates.append((offered, wanted, float(rate)))
    max_blue_lemonade = find_max_blue_lemonade(num_children, exchange_rates)
    print(f"{max_blue_lemonade:.10f}")

