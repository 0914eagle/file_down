

def cheese_count(cheese_list):
    cheese_dict = {}
    for cheese in cheese_list:
        if cheese[1] in cheese_dict:
            cheese_dict[cheese[1]] += 1
        else:
            cheese_dict[cheese[1]] = 1
    return cheese_dict

def main():
    n = int(input())
    cheese_list = []
    for i in range(n):
        cheese = input().split()
        cheese_list.append(cheese)
    cheese_dict = cheese_count(cheese_list)
    print(len(cheese_dict))

if __name__ == '__main__':
    main()

