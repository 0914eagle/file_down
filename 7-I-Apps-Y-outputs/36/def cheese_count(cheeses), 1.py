
def cheese_count(cheeses):
    cheese_dict = {}
    for cheese in cheeses:
        cheese_type = cheese[1]
        if cheese_type in cheese_dict:
            cheese_dict[cheese_type] += 1
        else:
            cheese_dict[cheese_type] = 1
    return cheese_dict

def main():
    n = int(input())
    cheeses = []
    for i in range(n):
        cheese = input().split()
        cheeses.append(cheese)
    cheese_dict = cheese_count(cheeses)
    print(cheese_dict['hard'] - cheese_dict['soft'])

if __name__ == "__main__":
    main()

