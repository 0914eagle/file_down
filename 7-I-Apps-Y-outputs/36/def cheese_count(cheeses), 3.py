


def cheese_count(cheeses):
    cheese_dict = {}
    for cheese in cheeses:
        cheese_type = cheese.split()[1]
        if cheese_type in cheese_dict:
            cheese_dict[cheese_type] += 1
        else:
            cheese_dict[cheese_type] = 1
    return cheese_dict


def main():
    n = int(input())
    cheeses = []
    for _ in range(n):
        cheeses.append(input())
    cheese_dict = cheese_count(cheeses)
    print(len(cheese_dict))


if __name__ == "__main__":
    main()

