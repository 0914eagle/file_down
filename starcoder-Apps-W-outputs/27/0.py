
def get_input():
    n = int(input())
    names = list(input() for _ in range(n))
    return names

def get_sorted_names(names):
    return sorted(names)

def get_sorted_names_in_lexicographical_order(names):
    names = sorted(names)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    sorted_names = []
    for name in names:
        new_name = ""
        for letter in name:
            new_name += alphabet[0]
            alphabet = alphabet[1:]
        sorted_names.append(new_name)
    return sorted_names

def get_letters_order(sorted_names):
    names = get_sorted_names(sorted_names)
    sorted_names_in_lexicographical_order = get_sorted_names_in_lexicographical_order(sorted_names)
    order = {}
    for name, sorted_name in zip(names, sorted_names_in_lexicographical_order):
        for i in range(len(name)):
            order[sorted_name[i]] = name[i]
    return order

def get_letters_order_as_string(letters_order):
    return "".join(list(letters_order.values()))

def get_result(sorted_names):
    letters_order = get_letters_order(sorted_names)
    return get_letters_order_as_string(letters_order)

def main():
    names = get_input()
    print(get_result(names))

if __name__ == '__main__':
    main()
